# MedicalSoftwareDevelopment
## Exercise 1: Gene Info
Exercise: 
Write a piece of code to answer the following questions: 1. How many genes are listed?
2. How many genes are listed for the species Homo Sapiens? 3. List all gene types
4. Which gene type occurs the most?

I uploaded two approaches for this exercise, each with it's advantages and disadvantages.

### Solution 1: Line by Line with Ruby
Files for this approach: exercise_1.rb, test_script.rb, md5_test_genes.tsv
The exercise is solved in exercise_1.rb and the tests to check whether the methods are working can be called by running the test_script.rb file. To properly execute it, the md5_test_genes.tsv file is required to check whether the processing of the initial file is handled correctly.
I would opt for this approach if I needed to quickly get some information from the dataset and the calculations were not too complicated. 

Advantages:
- Simplicity: direct & easy approach of processing the tsv file line by line
- Fast
- no dependency on db

Disadvantages:
- Scalability: file is very large
- Memory Constraints: Handling the entire dataset in memory can be impractical or impossible with very large datasets.

### Solution 2: Gene DB with SQL and Python
Files for this approach: db_setup.ipynb, db_logic.py (+ genes.db, which is generated from the initial gene_info file)
I would choose this approach, if I needed to do repeated analysis on the data and needed more complex queries.

Advantages:
- Scalability: can handle the large amount of the data well
- possibility for more complex queries with SQL databases
- Data Integrity: can help ensure the consistency of the data
- Python + SQL easy & powerful in combination
  
Disadvantages:
- longer setup time
- dependency on database

(Mainly used this second approach as a challenge to improve my personal skills with Python & SQL in combination :))
