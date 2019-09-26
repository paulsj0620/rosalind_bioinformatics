#! /usr/bin/python
# -*- coding : utf-8 -*-
ref_table = {'UUC' : 'F', 'UUU' : 'F', 'UUA' : 'L', 'UUG' : 'L', \
             'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L', \
             'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I', 'AUG' : 'M', \
             'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V', \
                'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S', \
                'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', \
                'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T', \
                'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A', \
                    'UAU' : 'Y', 'UAC' : 'Y', 'UAA' : '!', 'UAG' : '!', \
                    'CAU' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', \
                    'AAU' : 'N', 'AAC' : 'N', 'AAA' : 'K', 'AAG' : 'K', \
                    'GAU' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E', \
                        'UGU' : 'C', 'UGC' : 'C', 'UGA' : 'W', 'UGG' : 'W', \
                        'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', \
                        'AGU' : 'S', 'AGC' : 'S', 'AGA' : 'R', 'AGG' : 'R', \
                        'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G'}

input_data = open("rosalind_prot.txt", 'r')
input_seq = input_data.readlines()[0]

sequence = input_seq.upper()
codon = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
pocket = []
for i in codon :
    amino = ref_table.get(i)
    pocket.append(amino)
    if amino == None :
        amino = ''
print("".join(pocket[:-2]))