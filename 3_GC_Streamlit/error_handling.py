import streamlit as st
import logging
from logging_config import setup_logging

class EntryCheckError(Exception):
    pass

def handle_errors(e):
    st.warning(f"Operation unsuccessful: {e}")
    logging.error(f"Error - Operation unsuccessful: {e}")