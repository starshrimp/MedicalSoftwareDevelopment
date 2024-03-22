import logging

def setup_logging():
    # Configure the logging system to log messages to a file
    logging.basicConfig(
        level=logging.DEBUG,  # Adjust the logging level as needed
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='app.log',  # Log messages will be written to app.log
        filemode='a'  # Append mode, which ensures logs are added to the file; use 'w' for write mode to overwrite
    )

    # Test logging at all levels
    logging.debug('Debug message: This will get logged to a file.')
    logging.info('Info message: This will get logged to a file.')
    logging.warning('Warning message: This will get logged to a file.')
    logging.error('Error message: This will get logged to a file.')
    logging.critical('Critical message: This will get logged to a file.')
