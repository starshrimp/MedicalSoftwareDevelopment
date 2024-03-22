import streamlit as st
import pandas as pd
from io import StringIO
from Bio import SeqIO
from fasta_class import FastaClass
# from Bio.SeqUtils import GC
from gc_content import output_gc_content


def process_fasta_from_file(uploaded_file):
    all_entries = []
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        for record in SeqIO.parse(stringio, "fasta"):
            fasta = FastaClass(record.id, record.seq)
            all_entries.append(fasta)

    return all_entries

def display_results_from_file(file_entries):
    if file_entries:
        for entry in file_entries:
            output_gc_content(entry.id, entry.seq)
