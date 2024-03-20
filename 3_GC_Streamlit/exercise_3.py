import sys
import os
import streamlit as st
from Bio import SeqIO


# Exception classes for error handling
class InvalidEntryIDError(Exception):
    pass

class EmptySequenceError(Exception):
    pass

def main():
    file_path = check_filename()
    try:
        valid_entries, invalid_entries = validate_fasta_file(file_path)
        output(valid_entries, invalid_entries)
    except Exception as e:
        print(f"An error occurred: {e}")

def check_filename():
    if len(sys.argv) != 2:
        print("Please enter it in the format like this: python exercise_1.py FILENAME")
        sys.exit(1)
    file_path = sys.argv[1]
    if not is_file_readable_and_not_empty(file_path):
        sys.exit(1)
    return file_path

def is_file_readable_and_not_empty(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            with open(file_path, 'r') as file:
                return True
        except IOError:
            print(f"Error: The file '{file_path}' cannot be read.")
            return False
    else:
        print(f"Error: The file '{file_path}' does not exist or is empty.")
        return False

def validate_fasta_file(file_path):
    valid_entries = []
    invalid_entries = []
    for record in SeqIO.parse(file_path, "fasta"):
        if valid_entry(record):
            valid_entries.append(record)
        else:
            invalid_entries.append(record)
    return valid_entries, invalid_entries

def valid_entry(entry):
    try:
        return entry.id and entry.seq
    except Exception:
        return False

def output(valid_entries, invalid_entries):
    process_valid_entries(valid_entries)
    process_invalid_entries(invalid_entries)

def process_valid_entries(valid_entries):
    for entry in valid_entries:
        print(f"Entry ID: {entry.id}")
        print(f"GC Content Percentage: {count_gc(entry.seq) * 100:.10f}%\n")
    print(f"Total valid entries: {len(valid_entries)} \n")

def count_gc(seq):
    gc = sum(seq.upper().count(x) for x in ['G', 'C'])
    return gc / len(seq) if seq else 0

def process_invalid_entries(invalid_entries):
    for entry in invalid_entries:
        print(f"Invalid FASTA entry found: {entry.id}")
    if invalid_entries:
        print(f"Total invalid entries: {len(invalid_entries)}")

if __name__ == "__main__":
    main()
