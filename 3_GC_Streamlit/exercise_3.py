"""
Provides functionality for validating FASTA files to ensure entries are correct and complete.

Handles command line input for specifying the FASTA file path, checks for file validity, 
parses FASTA entries using Biopython, separates entries into valid and invalid categories 
based on presence of essential data fields. The module provides detailed output on the validity of 
entries, including specific error handling for common file and entry issues.

Classes:
    InvalidEntryIDError: Custom exception for invalid entry IDs.
    EmptySequenceError: Custom exception for entries with empty sequences.

Functions:
    main(): Orchestrates the file checking and validation process.
    check_filename(): Checks for proper command line input and file existence.
    is_file_readable_and_not_empty(file_path): Verifies if the file is readable and not empty.
    validate_fasta_file(file_path): Parses the FASTA file and categorizes entries.
    valid_entry(entry): Checks if an entry has both an ID and a sequence.
    output(valid_entries, invalid_entries): Manages the output of validation results.
    process_valid_entries(valid_entries): Processes and displays information for valid entries.
    count_gc(seq): Calculates the GC content percentage of a sequence.
    process_invalid_entries(invalid_entries): Processes and displays information for 
    nvalid entries.
"""

import sys
import os
from Bio import SeqIO

# Exception classes for error handling
class InvalidEntryIDError(Exception):
    """
    Exception raised for errors that occur due to an invalid entry ID in a FASTA file.

    Attributes:
        message (str): Explanation of the error
    """

    def __init__(self, message="Invalid entry ID found in FASTA file"):
        self.message = message
        super().__init__(self.message)

class EmptySequenceError(Exception):
    """
    Exception raised for errors that occur due to an empty sequence in a FASTA entry.

    Attributes:
        message (str): Explanation of the error
    """

    def __init__(self, message="Empty sequence found in FASTA entry"):
        self.message = message
        super().__init__(self.message)

def main():
    """
    Main function that runs the validation process for a FASTA file provided via command
    line argument.
    Handles exceptions and coordinates the output of validation results.
    """
    file_path = check_filename()
    try:
        valid_entries, invalid_entries = validate_fasta_file(file_path)
        output(valid_entries, invalid_entries)
    except Exception as e:
        print(f"An error occurred: {e}")

def check_filename():
    """
    Checks and validates the command line input to ensure a file path is provided and valid.
    Exits the script if the conditions are not met.

    Returns:
    str: Valid file path input from the command line.
    """
    if len(sys.argv) != 2:
        print("Please enter it in the format like this: python exercise_1.py FILENAME")
        sys.exit(1)
    file_path = sys.argv[1]
    if not is_file_readable_and_not_empty(file_path):
        sys.exit(1)
    return file_path

def is_file_readable_and_not_empty(file_path):
    """
    Checks if the file exists, is not empty, and is readable.

    Args:
    file_path (str): The path to the file to be checked.

    Returns:
    bool: True if the file is readable and not empty, False otherwise.
    """
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            with open(file_path, 'r'):
                return True
        except IOError:
            print(f"Error: The file '{file_path}' cannot be read.")
            return False
    else:
        print(f"Error: The file '{file_path}' does not exist or is empty.")
        return False

def validate_fasta_file(file_path):
    """
    Parses the FASTA file, validating each entry to determine if it's correctly 
    formatted and complete.

    Args:
    file_path (str): The path to the FASTA file.

    Returns:
    tuple: Two lists containing valid and invalid entries respectively.
    """
    valid_entries = []
    invalid_entries = []
    for record in SeqIO.parse(file_path, "fasta"):
        if valid_entry(record):
            valid_entries.append(record)
        else:
            invalid_entries.append(record)
    return valid_entries, invalid_entries

def valid_entry(entry):
    """
    Validates an individual FASTA entry to ensure it has both an ID and a non-empty sequence.

    Args:
    entry (SeqRecord): The FASTA entry to validate.

    Returns:
    bool: True if the entry is valid, False otherwise.
    """
    try:
        return entry.id and entry.seq
    except Exception:
        return False

def output(valid_entries, invalid_entries):
    """
    Manages the output of validation results by processing both valid and invalid FASTA entries.

    Args:
    valid_entries (list): A list of valid SeqRecord objects.
    invalid_entries (list): A list of invalid SeqRecord objects.
    """
    process_valid_entries(valid_entries)
    process_invalid_entries(invalid_entries)

def process_valid_entries(valid_entries):
    """
    Outputs details for valid FASTA entries including GC content and entry count.

    Args:
    valid_entries (list): A list of valid SeqRecord objects.
    """
    for entry in valid_entries:
        print(f"Entry ID: {entry.id}")
        print(f"GC Content Percentage: {count_gc(entry.seq) * 100:.10f}%\n")
    print(f"Total valid entries: {len(valid_entries)} \n")

def count_gc(seq):
    """
    Calculates the GC content of a sequence.

    Args:
    seq (str): The DNA sequence.

    Returns:
    float: The GC content percentage of the sequence.
    """
    gc = sum(seq.upper().count(x) for x in ['G', 'C'])
    return gc / len(seq) if seq else 0

def process_invalid_entries(invalid_entries):
    """
    Outputs details for invalid FASTA entries and the total count of such entries.

    Args:
    invalid_entries (list): A list of invalid SeqRecord objects.
    """
    for entry in invalid_entries:
        print(f"Invalid FASTA entry found: {entry.id}")
    if invalid_entries:
        print(f"Total invalid entries: {len(invalid_entries)}")

if __name__ == "__main__":
    main()
