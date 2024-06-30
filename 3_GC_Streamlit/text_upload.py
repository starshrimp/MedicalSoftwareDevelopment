"""
This module provides web-based tools to calculate GC content from user-provided FASTA sequences.
Utilizes Streamlit for UI interactions, processing FASTA sequences and displaying 
GC content results.

Dependencies:
- streamlit: For creating the web application interface.
- Bio.SeqIO: For parsing FASTA formatted sequences.
- custom modules: `fasta_class`, `error_handling`, `gc_content` for managing FASTA records and 
errors and calculating GC content.
"""


from io import StringIO
from Bio import SeqIO
import streamlit as st
from fasta_class import FastaRecord
from error_handling import handle_errors, EntryCheckError
from gc_content import output_gc_content


def display_results_from_text(fasta):
    """
    Triggers GC content calculation for provided FASTA sequences via a Streamlit button.

    Args:
        fasta (str): User-provided FASTA sequences as a string.

    Uses a button to start GC content calculations. 
    Catches and handles exceptions using a custom error handler.
    """
    if st.button('Calculate GC Content'):
        try:
            process_fasta_from_textinput(fasta)
        except Exception as e:
            handle_errors(e)

def process_fasta_from_textinput(fasta):
    """
    Processes FASTA sequences from text input, verifies them, and outputs GC content.

    Args:
        fasta (str): FASTA formatted text.

    Raises:
        EntryCheckError: If the entries are invalid or do not meet requirements.
    
    Parses FASTA data, checks validity, and uses output_gc_content to display GC content 
    for each valid entry.
    """
    text_entries = []
    text_entries = parse_fasta_from_string(fasta)

    if check_entry(text_entries):
        for entry in text_entries:
            output_gc_content(entry.id, entry.seq)
    else:
        raise EntryCheckError("Please enter a valid FASTA.")


def parse_fasta_from_string(fasta_string):
    """
    Converts a string containing FASTA formatted data into FastaRecord objects.

    Args:
        fasta_string (str): FASTA data as a string.

    Returns:
        list: A list of FastaRecord instances parsed from the input string.
    
    Parses FASTA entries using Bio.SeqIO from an in-memory string.
    """
    text_entries = []
    fasta_io = StringIO(fasta_string)

    for record in SeqIO.parse(fasta_io, "fasta"):
        entry = FastaRecord(record.id, record.seq)
        text_entries.append(entry)
    return text_entries


def check_entry(text_entries):
    """
    Checks if any of the FASTA entries contain sequences.

    Args:
        text_entries (list): List of FastaRecord objects.

    Returns:
        bool: True if at least one entry has a non-empty sequence, False otherwise.
    
    Validates that there are entries with sequences available for further processing.
    """
    return any(entry.seq for entry in text_entries)
