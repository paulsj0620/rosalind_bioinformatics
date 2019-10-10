#python 2.7 env
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Complementing a Strand of DNA')
    parser.add_argument('-i', '--input', metavar='path', required=False, help='If you want to input your txt file path')
    parser.add_argument('-HD', metavar='Homozygous Dominant', required=False, help='Homozygous Dominant')
    parser.add_argument('-HT', metavar='Heterozygous', required=False, help='Heterozygous')
    parser.add_argument('-HR', metavar='Homozygous Recessive', required=False, help='Homozygous Recessive')
    args = parser.parse_args()

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

def input_method(path) :
    input_data = open(path, 'r')
    for line in input_data :
        return line
def translate(input_seq) :
    sequence = input_seq.upper()
    codon = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    pocket = []
    for i in codon :
        amino = ref_table.get(i)
        pocket.append(amino)
        if amino == None :
            amino = ''
    print("".join(pocket[:-2]))

seq = input_method(args.input)
translate(seq)