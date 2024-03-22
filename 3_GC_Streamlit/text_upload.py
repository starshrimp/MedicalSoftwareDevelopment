import streamlit as st
from io import StringIO
from Bio import SeqIO
from fasta_class import FastaRecord
# from Bio.SeqUtils import GC
from gc_content import output_gc_content

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

def parse_fasta_from_string(fasta_string):
    text_entries = []
    fasta_io = StringIO(fasta_string)

    for record in SeqIO.parse(fasta_io, "fasta"):
        entry = FastaRecord(record.id, record.seq)  
        text_entries.append(entry)
    return text_entries


def check_entry(text_entries):
    return any(entry.seq for entry in text_entries)
