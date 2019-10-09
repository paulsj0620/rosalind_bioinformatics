import argparse
import string
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Complementing a Strand of DNA')
    parser.add_argument('-i', '--input', metavar='path', required=True, help='Your input file path')
    args = parser.parse_args()

def input_method(path) :
    input = open(path, 'r' )
    for line in input :
        return line

def complement(dna) :
    table = string.maketrans('ATGC','TACG')
    rep = dna.translate(table)
    return rep[::-1]

input_dna = input_method(args.input)
print(complement(input_dna))