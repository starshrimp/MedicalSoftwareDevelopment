"""
Provides functionality to configure and initialize logging for Python applications.

Function:
    setup_logging(): Configures the logging to capture messages with debug and higher severity levels into a file.

Example Usage:
    Simply import and call setup_logging at the beginning of your application to start logging.
"""

import logging

def setup_logging():
    """
    Configure the  logging system to log messages to a file with a specified format.

    No parameters are used and no values are returned. 

    Usage:
        Call this function at the start of your application to ensure all  
        operations are logged.
    """
    # Configure the logging system to log messages to a file
    logging.basicConfig(
        level=logging.DEBUG,  # Adjust the logging level as needed
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='app.log',  # Log messages will be written to app.log
        filemode='a'  # Append mode, which ensures logs are added to the file
    )
