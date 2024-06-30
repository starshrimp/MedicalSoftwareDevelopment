"""
This module provides error handling capabilities for a Streamlit web application. It includes 
definitions for custom exception classesand functions for handling exceptions within 
the application.

Classes:
    EntryCheckError: A custom exception for entry validation failures in the application.

Functions:
    handle_errors(e): Logs and displays warnings for exceptions using Streamlit and the logging 
    module.

External Modules:
    logging_config: Configures the logging for the application.
    streamlit: Used to display warnings and messages in the web interface.
"""

import logging
import streamlit as st
from logging_config import setup_logging

class EntryCheckError(Exception):
    pass

def handle_errors(e):
    """
    Handle exceptions by logging them and displaying a warning message through the 
    Streamlit interface.

    Args:
        e (Exception): The exception to handle, typically caught during application operations.

    This function logs the error and displays a user-friendly warning in the Streamlit app, ensuring
    that errors are both recorded for debugging and communicated to the user.
    """
    st.warning(f"Operation unsuccessful: {e}")
    logging.error("Error - Operation unsuccessful: %s", e)
