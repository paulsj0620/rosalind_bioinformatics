input = open("rosalind_rna.txt", 'r')
dna_str = input.readline()
dna_str = dna_str.upper()
rna_str = dna_str.replace("T","U")
print(rna_str)
input.close
