"""
This module provides tools for DNA and protein sequence manipulation, including
transcription, translation, and random sequence generation. It utilizes the Singleton
design pattern for sequence storage and employs a factory pattern for sequence creation.

Classes:
    DNASequenceTranslator: Provides static methods for DNA transcription and translation.
    SequenceFactory: Factory class for creating random DNA or protein sequences.
    SequenceStorage: Singleton class for storing and managing sequence data.
    SequenceGenerator: Abstract base class for sequence generators.
    DNASequenceGenerator: Generates random DNA sequences.
    ProteinSequenceGenerator: Generates random protein sequences.
    ...

Functions:
    main(): Entry point for the module, orchestrating the sequence operations.
    initialize_sequence(): Initializes a DNA sequence from command line or default.
    initialize_storage(sequence): Initializes the sequence storage with a given DNA sequence.
    transcribe_and_translate(storage): Handles transcription and translation of DNA sequence.
    output(storage): Prints the stored sequences.

Usage:
    Run the module directly to perform sequence operations and output the results.
"""

import sys
import random
from abc import ABC, abstractmethod
from Bio.Seq import Seq


class DNASequenceTranslator:
    """
    Provides static methods for DNA transcription to RNA and RNA translation to protein.

    Static Methods:
        transcribe_dna_to_rna(dna, storage): Transcribes DNA to RNA, stores the result.
        translate_rna_to_protein(rna, storage): Translates RNA to protein, stores the result.
    """
    # this is a utility class containing static methods
    @staticmethod
    def transcribe_dna_to_rna(dna, storage):
        dna_seq_obj = Seq(dna)
        result = dna_seq_obj.transcribe()
        storage.save('RNA', result)
        # return result, storage

    @staticmethod
    def translate_rna_to_protein(rna, storage):
        result = rna.translate()
        storage.save('Protein', result)
        # return storage #returns the storage object


class SequenceFactory:
    """
    Factory class for creating sequences based on specified type ('DNA' or 'Protein').

    Static Methods:
        create_sequence(type): Creates a sequence of the specified type.
        generate_random_DNA_sequence(): Generates, prints a random DNA sequence.
        generate_random_protein_sequence(): Generates, prints a random protein sequence.
    """
    @staticmethod
    def create_sequence(type):
        if type == "DNA":
            SequenceFactory.generate_random_DNA_sequence()
        elif type == "Protein":
            SequenceFactory.generate_random_protein_sequence()

    @staticmethod
    def generate_random_DNA_sequence():
        # Creating a random Sequence with DNASequenceGenerator
        dna_generator = DNASequenceGenerator()
        random_dna_seq = dna_generator.create_sequence(20)
        print("Random DNA Sequence:", random_dna_seq)

    @staticmethod
    def generate_random_protein_sequence():
        # Creating a random Sequence with ProteinSequenceGenerator
        protein_generator = ProteinSequenceGenerator()
        random_protein_seq = protein_generator.create_sequence(20)
        print("Random Protein Sequence:", random_protein_seq)


class SequenceStorage():
    """
    Singleton class for managing the storage of biological sequences.

    Attributes:
        data (dict): Dictionary to store sequences with type labels.

    Methods:
        save(name, seq): Saves a sequence with its type label.
        read(name): Retrieves a sequence by its type label.
    """
    # this holds the instance that will be created
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = {}
        return cls._instance

    def save(self, name, seq):
        self.data[name] = seq

    def read(self, name):
        return self.data[name]


class SequenceGenerator(ABC):
    """
    Abstract base class for sequence generators.

    This class defines a template for creating sequences, ensuring that all concrete
    implementations provide their own sequence creation methods.

    Methods:
        create_sequence(n): Abstract method to create a sequence of length n.
    """
    # this is an abstract base class so the individual classes
    # can make use of polymorphism
    @abstractmethod
    def create_sequence(self, n):
        pass


class DNASequenceGenerator(SequenceGenerator):
    """
    Generates random DNA sequences. Inherits from SequenceGenerator.

    Attributes:
        alphabet (list): List of DNA nucleotides (A, C, G, T).

    Methods:
        create_sequence(n): Generates a random DNA sequence of length n.
    """
    # individual class using polymorphism
    alphabet = ['A', 'C', 'G', 'T']

    def create_sequence(self, n):
        result = ''
        for i in range(n):
            idx = random.randint(0, len(DNASequenceGenerator.alphabet) - 1)
            result = result + DNASequenceGenerator.alphabet[idx]
        return result


class ProteinSequenceGenerator(SequenceGenerator):
    """
    Generates random protein sequences. Inherits from SequenceGenerator.

    Attributes:
        amino_acids (list): List of standard amino acids one-letter codes.

    Methods:
        create_sequence(n): Generates a random protein sequence of length n.
    """
    # individual class 2 with polymorphism
    # List of one-letter codes for standard amino acids
    amino_acids = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

    def create_sequence(self, n):
        result = ''
        for i in range(n):
            idx = random.randint(0, len(ProteinSequenceGenerator.amino_acids) - 1)
            result = result + ProteinSequenceGenerator.amino_acids[idx]
        return result


def main():
    """
    Main function to orchestrate sequence operations and output results.
    """
    sequence = initialize_sequence()
    storage = initialize_storage(sequence)

    SequenceFactory.create_sequence("DNA")
    SequenceFactory.create_sequence("Protein")

    transcribe_and_translate(storage)
    output(storage)


def initialize_sequence():
    """
    Initializes a DNA sequence from command line input or default.

    Returns:
        str: A DNA sequence.
    """
    if len(sys.argv) == 2:
        sequence = sys.argv[1]
    else:
        sequence = "GTGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
    return sequence


def initialize_storage(sequence):
    """
    Initializes the SequenceStorage with a given DNA sequence.

    Args:
        sequence (str): A DNA sequence to initially store.

    Returns:
        SequenceStorage: An initialized singleton storage object.
    """
    storage = SequenceStorage()
    storage.save('DNA', sequence)
    return storage


def transcribe_and_translate(storage):
    """
    Manages transcription of DNA to RNA and translation to protein, storing results.

    Args:
        storage (SequenceStorage): Singleton storage object with the DNA sequence.
    """
    DNASequenceTranslator.transcribe_dna_to_rna(storage.read('DNA'), storage)
    DNASequenceTranslator.translate_rna_to_protein(storage.read('RNA'), storage)
    # return storage


def output(storage):
    """
    Outputs stored DNA, RNA, and protein sequences from the storage.

    Args:
        storage (SequenceStorage): Singleton storage to read sequences from.
    """
    print("\nOriginal Sequences: ")
    print("DNA Sequence:", storage.read('DNA'))
    print("RNA Sequence:", storage.read('RNA'))
    print("Protein Sequence:", storage.read('Protein'))


if __name__ == '__main__':
    main()
