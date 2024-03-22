import sys
import os
import streamlit as st
from Bio import SeqIO
from io import StringIO
from file_upload import process_fasta_from_file
from fasta_class import FastaClass


def main():
    fasta, file_entries = setup()
    display_results_from_file(file_entries)
    display_results_from_text(fasta)

def setup():
    st.title('GC Content Calculator')
    st.caption('To calculate the GC content of a fasta file, please upload a fasta file beneath or enter a FASTA sequence in the text box below.')
    fasta = st.text_area('FASTA Sequence')
    uploaded_file = st.file_uploader("Upload your FASTA file", type=['fasta', 'fna'])
    file_entries = process_fasta_from_file(uploaded_file)
    return fasta, file_entries

def calculate_gc_content(fasta):
    gc = sum(fasta.upper().count(x) for x in ['G', 'C'])
    return gc / len(fasta) if fasta else 0

def output_gc_content(id, seq):
    st.text(f"FASTA Record ID: {id} \n GC Content Percentage: {calculate_gc_content(seq) * 100:.10f}%\n")

def display_results_from_file(file_entries):
    if file_entries:
        for entry in file_entries:
            output_gc_content(entry.id, entry.seq)

def display_results_from_text(fasta):
    if st.button('Calculate GC Content'):
        if fasta:
            process_fasta_from_textinput(fasta)
        else:
            st.warning('Please enter a valid FASTA sequence')

def process_fasta_from_textinput(fasta):
    text_entries = []
    text_entries = parse_fasta_from_string(fasta)

    if check_entry(text_entries):
        for entry in text_entries:
            output_gc_content(entry.id, entry.seq)

def check_entry(text_entries):
    if text_entries:
        for entry in text_entries:
            if entry.seq:
                return True
            else:
                return False
    else:
        False

def parse_fasta_from_string(fasta_string):
    text_entries = []
    fasta_io = StringIO(fasta_string)

    for record in SeqIO.parse(fasta_io, "fasta"):
        entry = FastaClass(record.id, record.seq)  
        text_entries.append(entry)
    return text_entries

main()


