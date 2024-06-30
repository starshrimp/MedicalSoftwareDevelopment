"""
Provides functionality for calculating the GC content of DNA sequences presented in FASTA format,
displays these calculations using the Streamlit library for interactive web applications.

Functions:
    calculate_gc_content(fasta): Computes the GC content of a given DNA sequence.
    output_gc_content(id, seq): Displays the GC content and sequence ID using Streamlit.

Dependencies:
    Streamlit: A framework for creating web applications for machine learning and data science.

Example Usage:
    This script is intended to be run within a Streamlit application environment.
"""

import streamlit as st


def calculate_gc_content(fasta):
    """
    Calculate the GC content of a DNA sequence.

    Args:
        fasta (str): The DNA sequence for which the GC content is calculated.

    Returns:
        float: The GC content of the sequence as a decimal, or 0 if the sequence is empty or 
        an error occurs.

    Raises:
        Displays a warning message using Streamlit if an exception occurs during calculation.
    """
    try:
        gc = sum(fasta.upper().count(x) for x in ['G', 'C'])
        return gc / len(fasta) if fasta else 0
    except Exception as e:
        st.warning(f"Error: {e}")
        return 0

def output_gc_content(id, seq):
    """
    Output the GC content percentage of a DNA sequence along with its ID using Streamlit.

    Args:
        id (str): The identifier for the FASTA sequence.
        seq (str): The DNA sequence whose GC content is to be calculated and displayed.

    This function calls calculate_gc_content to determine the GC content and then formats and 
    displays the results using Streamlit's text function.
    """
    st.text(f"FASTA Record ID: {id} \n GC Content Percentage: {calculate_gc_content(seq) * 100:.10f}%\n")
