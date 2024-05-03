import sys
import random
from abc import ABC, abstractmethod
from Bio.Seq import Seq

class DNASequenceTranslator: 
    #this is a utility class containing static methods
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
    @staticmethod
    def create_sequence(type):
        if type == "DNA":
            SequenceFactory.generate_random_DNA_sequence()  # Changed to a static call
        elif type == "Protein":
            SequenceFactory.generate_random_protein_sequence()  # Added () to actually call the method

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
    #this holds the instance that will be created
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
    #this is an abstract base class so the individual calsses can make use of polymorphism
    @abstractmethod
    def create_sequence(self,n):
        pass
    
class DNASequenceGenerator(SequenceGenerator):
    #individual class using polymorphism
    alphabet = ['A','C','G','T']
    def create_sequence(self, n):
        result = ''
        for i in range(n):
            idx = random.randint(0,len(DNASequenceGenerator.alphabet) - 1)
            result = result + DNASequenceGenerator.alphabet[idx]
        return result

class ProteinSequenceGenerator(SequenceGenerator):
    #individual class 2 with polymorphism
    # List of one-letter codes for standard amino acids
    amino_acids = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

    def create_sequence(self, n):
        result = ''
        for i in range(n):
            idx = random.randint(0,len(ProteinSequenceGenerator.amino_acids) - 1)
            result = result + ProteinSequenceGenerator.amino_acids[idx]
        return result
    

def main():
    sequence = initialize_sequence()
    storage = initialize_storage(sequence)

    SequenceFactory.create_sequence("DNA")
    SequenceFactory.create_sequence("Protein")

    transcribe_and_translate(storage)
    output(storage)


def initialize_sequence():
    if len(sys.argv) == 2:
        sequence = sys.argv[1]
    else:
        sequence = "GTGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
    return sequence

def initialize_storage(sequence):
    storage = SequenceStorage()
    storage.save('DNA', sequence)
    return storage

def transcribe_and_translate(storage):
    DNASequenceTranslator.transcribe_dna_to_rna(storage.read('DNA'), storage)
    DNASequenceTranslator.translate_rna_to_protein(storage.read('RNA'), storage)
    # return storage

def output(storage):
    print("\nOriginal Sequences: ")
    print("DNA Sequence:", storage.read('DNA'))
    print("RNA Sequence:", storage.read('RNA'))
    print("Protein Sequence:", storage.read('Protein'))


if __name__ == '__main__':
    main()
