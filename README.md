# MedicalSoftwareDevelopment
## Exercise 1: Gene Info
Exercise: 
Write a piece of code to answer the following questions: 
1. How many genes are listed?
2. How many genes are listed for the species Homo Sapiens? 
3. List all gene types
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

(Mainly used this second approach as a challenge to improve my personal skills with Python & SQL in combination :) )

## Exercise 2: GC Content
Given: A DNA sequence in FASTA format. Return: GC-content value for the given sequence.
Files:
- exercise_2.rb: main ruby file, interpreting the fasta with use of the ruby gem bio
- test_script_2.rb: includes tests for the methods check_filename (with testcases: no arguments, several arguments, nonexistent file, valid file) and validate_fasta_file! (with  testcases: valid fasta, invalid entry ID, empty sequence, mixed validity) to ensure proper function of these methods
- human_gene.fna: file with the FASTA entries for the human CD28 (downloaded from https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=940) 
- gene.fna: file with the FASTA entries for the mouse CD28 (also downloaded from ncbi)

### Questions
- What is the GC-content value of the Human Gene CD28? 40.0049335512% (first entry), 39.9975336807% (second entry)
- What is a fasta file? FASTA = format to store information on nucleic acid sequences, format  consists of: heade(starting with >, then name/id and further information like species, chromosome etc) and sequence 
- What happens if there are multiple sequences in the fasta file? -> each sequence is processed seperately
- What happens if the fasta file is invalid? -> an error is raised
- What happens if there are upper case and lower case letters in the sequence? -> both upper- and lowercase letters are included in the calculation; (FASTA typically converts lowercase letters to uppercase anyway, but as I was manually checking for G and C, I had to include search for g and c as well)
- Where to download a sequence for a human gene? e.g. NCBI