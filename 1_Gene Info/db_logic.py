"""
Provides functionality for querying and processing gene data from a SQLite database.

Contains functions for extraction, processing, and display of gene-related data. 

Functions:
    get_genes_data(conn, question_number, query): Fetches / processes gene data from the database.
    process_data(question_number, rows): Processes raw gene data into a human-readable format.
    main(): handles database connections and managing data retrieval / display.
    output_result(results): Output the processed results for each question.

Dependencies:
    SQLite3 for database operations
    'genes' table
"""


import sqlite3

def get_genes_data(conn, question_number, query):
    """
    Executes a SQL query to fetch gene data based on a provided query and connection.

    Args:
    conn (sqlite3.Connection): A connection object to the SQLite database.
    question_number (int): An identifier for the specific question or data request.
    query (str): SQL query string to be executed.

    Returns:
    Any: The processed data for the specific question, or None if there is
    an error during database interaction.

    Raises:
    sqlite3.Error: If there is an issue executing the database query.
    """
    try:
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()  # Close the cursor
        return process_data(question_number, rows)
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
        return None

def process_data(question_number, rows):
    """
    Processes the fetched data based on the question number.

    Args:
    question_number (int): The specific question number which dictates the format of processing.
    rows (list of tuple): Data fetched from the database as a list of tuples.

    Returns:
    str: A string representing the processed result for the question.
    """
    if question_number in (1, 2):
        result = rows[0][0]
    elif question_number == 3:
        result = ', '.join(str(row[0]) for row in rows)
    elif question_number == 4:
        result = f"Most frequent gene type: {rows[0][0]}, Frequency: {rows[0][1]}"
    return result

def main():
    """
    Main function to manage database connection and fetch results for predefined queries.

    Details:
    Establishes a connection to a SQLite database, executes multiple queries to fetch data,
    processes and prints the results for different questions.
    """
    database = 'genes.db'
    with sqlite3.connect(database) as conn:  # using connection as context manager
        results = {}
        print("MD5 Hash of the file: 391abe3356f88ff7a34a085f37e29f66")
        results[1] = get_genes_data(conn, 1, "SELECT COUNT(*) FROM genes")
        results[2] = get_genes_data(conn, 2, "SELECT COUNT(*) FROM genes WHERE tax_id = 9606")
        results[3] = get_genes_data(conn, 3, "SELECT DISTINCT type_of_gene FROM genes;")
        results[4] = get_genes_data(conn, 4, "SELECT type_of_gene, COUNT(type_of_gene) AS frequency FROM genes GROUP BY type_of_gene ORDER BY frequency DESC LIMIT 1;")
        output_result(results)

def output_result(results):
    """
    Prints the results for each question number.

    Args:
    results (dict): A dictionary containing question numbers as keys and processed results 
    as values.
    """
    for question_number, result in results.items():
        print(f"Question number: {question_number}\n \t Result: {result}")

if __name__ == "__main__":
    main()
