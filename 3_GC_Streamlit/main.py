import sys
import os
import streamlit as st
from Bio import SeqIO
from io import StringIO
import file_upload
from fasta_class import FastaClass


def main():
    setup()
    process_fasta_from_textinput()
    file_entries= file_upload.fasta_file_upload()
    for entry in file_entries:
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
    text_entries = []
    fasta = st.text_area('FASTA Sequence')
    text_entries = parse_fasta_from_string(fasta)
    if st.button('Calculate GC Content'):
        for entry in text_entries:
            output_gc_content(entry.id, entry.seq)


def parse_fasta_from_string(fasta_string):
    text_entries = []
    fasta_io = StringIO(fasta_string)

    for record in SeqIO.parse(fasta_io, "fasta"):
        entry = FastaClass(record.id, record.seq)  
        text_entries.append(entry)
    return text_entries

main()


