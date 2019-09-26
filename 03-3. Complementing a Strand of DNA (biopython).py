from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

input = open("rosalind_revc.txt", 'r')
dna_str = input.readline()
seq = Seq(dna_str, IUPAC.unambiguous_dna)
re_co_seq = seq.reverse_complement()
print(re_co_seq)
