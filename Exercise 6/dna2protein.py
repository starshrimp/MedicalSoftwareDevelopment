from Bio.Seq import Seq
import random
from abc import ABC, abstractmethod


class DNASequenceTranslator: 
    #this is a utility class containing static methods
    @staticmethod
    def transcribe_dna_to_rna(dna):
        result = dna.transcribe()
        storage.save('RNA', result)
        return result, storage
        
    @staticmethod
    def translate_rna_to_protein(rna):
        result = rna.translate()
        storage.save('Protein', result)
        return storage
    
    
# class SequenceStorage(ABC):
#     #this holds the instance that will be created

#     def save(self, name, seq):
#         pass

#     def read(self, name):
#         pass
    
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
            idx = random.randint(0,3)
            result = result + DNASequenceGenerator.alphabet[idx]
        return result

class ProteinSequenceGenerator(SequenceGenerator):
    #individual class 2 with polymorphism
    # List of one-letter codes for standard amino acids
    amino_acids = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

    def create_sequence(self, n):
        result = ''
        for i in range(n):
            idx = random.randint(0,19)
            result = result + ProteinSequenceGenerator.amino_acids[idx]
        return result
    



def output():
    print("Random DNA Sequence:", random_dna_seq)
    print("Random Protein Sequence:", random__protein_seq)

    print("Original Sequences: ")
    print("DNA Sequence:", storage.read('DNA'))
    print("RNA Sequence:", rna_seq_obj)
    #print("Protein Sequence:", protein_seq)



def main():
    output()

if __name__ == '__main__':

    sequence = 'GTGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG'
    storage = SequenceStorage()
    storage.save('DNA', sequence)
    #creating a Seq onject for the sequence
    dna_seq_obj = Seq(sequence)

    rna_seq_obj, storage = DNASequenceTranslator.transcribe_dna_to_rna(dna_seq_obj)
    
    # RNA to protein sequence
    stored_protein = DNASequenceTranslator.translate_rna_to_protein(rna_seq_obj)
    print("Protein from storage:", stored_protein.read("Protein"))
    # Create a new object of the SequenceStorage class
    # storage = SequenceStorage()
    # storage.save('DNA', sequence)
    print(storage.read('DNA'))
    print(storage.read('RNA'))
    print(storage.read('Protein'))

    # Creating a random Sequence with DNASequenceGeneratir
    dna_generator = DNASequenceGenerator()
    random_dna_seq = dna_generator.create_sequence(20)

    protein_generator = ProteinSequenceGenerator()
    random__protein_seq = protein_generator.create_sequence(20)
    main()


