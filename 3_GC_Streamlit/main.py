"""
This module creates a Streamlit web application to calculate the GC content of sequences
from FASTA files. Users can input FASTA sequences directly through a text box or by 
uploading a file. The application leverages several modules for processing and displaying
the results, including error handling and logging setup.

Functions:
    main(): Initializes the application and coordinates the input and output processes.
    setup(): Sets up the Streamlit interface and handles file or text inputs.

External Modules:
    file_upload: Handles processing of FASTA sequences uploaded as files.
    text_upload: Manages processing of FASTA sequences entered via text input.
    logging_config: Configures logging across the application.
    error_handling: Provides error handling mechanisms for robust application behavior.
"""

import streamlit as st
from file_upload import process_fasta_from_file, display_results_from_file
from text_upload import display_results_from_text
from logging_config import setup_logging
from error_handling import handle_errors

setup_logging()

def main():
    """
    Main function to initialize the logging and display functionalities within the 
    Streamlit web application. It orchestrates the sequence input through file or 
    text and displays the calculated GC content.
    """
    setup_logging()
    fasta, file_entries = setup()
    display_results_from_file(file_entries)
    display_results_from_text(fasta)

def setup():
    """
    Sets up the Streamlit web interface for GC content calculation, providing options for 
    text input and file upload.

    Returns:
        tuple: A tuple containing the text input FASTA sequence and the entries 
        processed from the uploaded file.

    This function configures the user interface elements including title, instructions, 
    text area for FASTA sequence input, and file uploader for FASTA files. It processes 
    the uploaded file to obtain FASTA entries if available.

    Exceptions:
        Handles any exceptions during file processing or input handling.
    """
    try: 
        st.title('GC Content Calculator')
        st.caption('To calculate the GC content of a fasta file, please upload a fasta file beneath or enter a FASTA sequence in the text box below.')
        fasta = st.text_area('FASTA Sequence')
        uploaded_file = st.file_uploader("Upload your FASTA file", type=['fasta', 'fna'])
        file_entries = process_fasta_from_file(uploaded_file)
    except Exception as e:
        handle_errors(e)
    return fasta, file_entries

main()
