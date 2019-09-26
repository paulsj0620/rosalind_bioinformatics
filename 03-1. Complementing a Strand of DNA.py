input = open("rosalind_revc.txt", 'r')
dna_str = input.readline()
table = str.maketrans('ATGC','TACG')
rep = dna_str.translate(table)
print(rep[::-1])
input.close
