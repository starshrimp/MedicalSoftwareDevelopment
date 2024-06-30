"""
This module defines the FastaRecord class, which is used for representing and handling 
FASTA record data. It provides a structured way to store sequence data and associated identifiers 
from FASTA formatted files.
"""

class FastaRecord:
    """
    Class to encapsulate a FASTA record's data.

    Attributes:
        id (str): The identifier of the FASTA record, typically describing the sequence.
        seq (str): The nucleotide or amino acid sequence of the FASTA record.

    This class provides a way to manage sequence data in a structured format, making it easier 
    to handle and process FASTA file data within bioinformatics applications.
    """
    def __init__(self, id, seq):
        """"
        Initializes a new FastaRecord with a specific ID and sequence.

        Args:
            id (str): The identifier of the FASTA record.
            seq (str or Bio.Seq): The sequence of the FASTA record, which will be stored as a 
            string.
        """
        self.id = id
        self.seq = str(seq)
