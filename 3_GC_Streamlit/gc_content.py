import streamlit as st


def calculate_gc_content(fasta):
    try:
        gc = sum(fasta.upper().count(x) for x in ['G', 'C'])
        return gc / len(fasta) if fasta else 0
    except Exception as e:
        st.warning(f"Error: {e}")
        return 0

def output_gc_content(id, seq):
    st.text(f"FASTA Record ID: {id} \n GC Content Percentage: {calculate_gc_content(seq) * 100:.10f}%\n")