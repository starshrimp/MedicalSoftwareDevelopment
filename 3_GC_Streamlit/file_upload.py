import streamlit as st
import pandas as pd
from io import StringIO
from Bio import SeqIO
from fasta_class import FastaClass
# from Bio.SeqUtils import GC

all_entries = []

def process_fasta_from_file():
    uploaded_file = st.file_uploader("Upload your FASTA file", type=['fasta', 'fna'])

    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        for record in SeqIO.parse(stringio, "fasta"):
            fasta = FastaClass(record.id, record.seq)
            all_entries.append(fasta)

    return all_entries

