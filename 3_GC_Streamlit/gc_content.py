import sys
import os
import streamlit as st
from Bio import SeqIO
from io import StringIO
from fasta_class import FastaClass

def calculate_gc_content(fasta):
    gc = sum(fasta.upper().count(x) for x in ['G', 'C'])
    return gc / len(fasta) if fasta else 0

def output_gc_content(id, seq):
    st.text(f"FASTA Record ID: {id} \n GC Content Percentage: {calculate_gc_content(seq) * 100:.10f}%\n")