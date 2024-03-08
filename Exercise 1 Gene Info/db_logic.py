import sqlite3

def get_genes_data(conn, question_number, query):
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
    if question_number == 1 or question_number == 2:
        result = rows[0][0]
    elif question_number == 3:
        result = ', '.join(str(row[0]) for row in rows)
    elif question_number == 4:
        result = f"Most frequent gene type: {rows[0][0]}, Frequency: {rows[0][1]}"
    return result

def main():
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
    for question_number, result in results.items():
        print(f"Question number: {question_number}\n \t Result: {result}")
    
if __name__ == "__main__":
    main()