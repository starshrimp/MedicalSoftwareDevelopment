import sys
import os
import streamlit as st
from Bio import SeqIO
from io import StringIO
import file_upload
from fasta_class import FastaClass






# # Exception classes for error handling
# class InvalidEntryIDError(Exception):
#     pass

# class EmptySequenceError(Exception):
#     pass


def main():
    setup()
    process_fasta_from_textinput()
    all_entries= file_upload.fasta_file_upload()
    for entry in all_entries:
        output_gc_content(entry.id, entry.seq)

def setup():
    st.title('GC Content Calculator')
    st.caption('To calculate the GC content of a fasta file, please upload a fasta file beneath or enter a FASTA sequence in the text box below.')


def calculate_gc_content(fasta):
    gc = sum(fasta.upper().count(x) for x in ['G', 'C'])
    return gc / len(fasta) if fasta else 0

def output_gc_content(id, seq):
    st.text(f"FASTA Record ID: {id} \n GC Content Percentage: {calculate_gc_content(seq) * 100:.10f}%\n")


def process_fasta_from_textinput():
    all_entries = []
    fasta = st.text_area('FASTA Sequence')
    all_entries = parse_fasta_from_string(fasta)
    if st.button('Calculate GC Content'):
        for entry in all_entries:
            output_gc_content(entry.id, entry.seq)


def parse_fasta_from_string(fasta_string):
    all_entries = []
    # Split the input string into entries based on '>'
    entries = fasta_string.strip().split('>')
    for entry in entries:
        if not entry:
            continue
        # Split each entry into lines
        lines = entry.split('\n')
        # The first line is the ID
        id = lines[0]
        # The rest are the sequence lines, which we join together
        seq = ''.join(lines[1:])
        # Create a FastaClass object and add it to the list
        all_entries.append(FastaClass(id, seq))
    return all_entries

main()


