import sys
import os
import streamlit as st
from Bio import SeqIO
from io import StringIO
from file_upload import process_fasta_from_file, display_results_from_file
from text_upload import display_results_from_text
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

main()


