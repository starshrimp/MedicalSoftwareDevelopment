"""
This module provides functionality to process FASTA files and display their GC content 
using Streamlit. It uses the BioPython library to parse FASTA entries, and handles file
input/output and error management.

Functions:
    process_fasta_from_file(uploaded_file): Process the FASTA file and store each record.
    display_results_from_file(file_entries): Display the GC content of the records from the 
    processed file.
"""

from io import StringIO
from Bio import SeqIO
from fasta_class import FastaRecord
from gc_content import output_gc_content
from error_handling import handle_errors

def process_fasta_from_file(uploaded_file):
    """
    Processes a FASTA file uploaded by the user, parsing each entry and creating FastaRecord
    objects.

    Args:
        uploaded_file (UploadedFile): The file uploaded by the user, expected to be in FASTA format.
    
    Returns:
        list: A list of FastaRecord instances representing the entries in the uploaded FASTA file.

    Raises:
        Exception: Any exceptions that occur during file reading or parsing are caught and handled 
        by the handle_errors function.

    This function reads from the provided UploadedFile object, decodes it to a string, and then 
    parses it using SeqIO.
    It constructs a list of FastaRecord objects which encapsulate the ID and sequence of each entry 
    in the FASTA file.
    """
    all_entries = []

    try:
        if uploaded_file is not None:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

            for record in SeqIO.parse(stringio, "fasta"):
                fasta = FastaRecord(record.id, record.seq)
                all_entries.append(fasta)
    except Exception as e:
        handle_errors(e)

    return all_entries

def display_results_from_file(file_entries):
    """
    Displays the GC content of each entry in the provided list of FastaRecord objects using the 
    Streamlit library.

    Args:
        file_entries (list): A list of FastaRecord objects whose GC content is to be displayed.

    This function iterates over each FastaRecord in the provided list, extracting the ID and 
    sequence.
    It then uses the output_gc_content function to calculate and display the GC content for 
    each sequence.
    """
    if file_entries:
        for entry in file_entries:
            output_gc_content(entry.id, entry.seq)
