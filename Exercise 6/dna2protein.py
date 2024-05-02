from Bio.Seq import Seq
import random

class DNASequenceTranslator:
    staticmethod
    def transcribe_dna_to_rna(dna):
        result = dna.transcribe()
        return result

    staticmethod
    def translate_rna_to_protein(rna):
        result = rna.translate()
        return result
    
class SequenceStorage:

    def __init__(self):
        self.data = {}

    def save(self, name, seq):
        self.data[name] = seq

    def read(self, name):
        return self.data[name]
    
class DNASequenceGenerator:
    alphabet = ['A','C','G','T']
    def create_sequence(self, n):
        result = ''
        for i in range(n):
            idx = random.randint(0,3)
            result = result + DNASequenceGenerator.alphabet[idx]
        return result


if __name__ == '__main__':

    sequence = 'GTGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG'

    #creating a Seq onject for the sequence
    dna_seq_obj = Seq(sequence)

    

    rna_seq_obj = DNASequenceTranslator.transcribe_dna_to_rna(dna_seq_obj)
    
    # RNA to protein sequence
    protein_seq = DNASequenceTranslator.translate_rna_to_protein(rna_seq_obj)
    
    print("DNA Sequence:", sequence)
    print("RNA Sequence:", rna_seq_obj)
    print("Protein Sequence:", protein_seq)
