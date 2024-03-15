import sys
import os

def main():
  file_path = check_filename()

def check_filename():
    if len(sys.argv[1]) != 1:
        print("Please provide the file path")
        sys.exit(1)
    else:
        is_file_readable_and_not_empty(sys.argv[1])
  
  
def is_file_readable_and_not_empty(file_path):
    # Check if the file exists and is not empty
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            # Try opening the file to check if it's readable
            with open(file_path, 'r') as file:
                # If this succeeds, the file is readable
                return True
            file_path = sys.argv[1]
        except IOError:
            # If an IOError is raised, the file is not readable
            print(f"Error: The file '{file_path}' cannot be read.")
            return False
    else:
        print(f"Error: The file '{file_path}' does not exist or is empty.")
        return False