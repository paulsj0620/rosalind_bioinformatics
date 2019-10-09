import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Counting DNA Nucleotides')
    parser.add_argument('-o', '--option', help='Choose Nucleotide (A, C, G, T) (Default: Count All Nucleotide)')
    args = parser.parse_args()

def input_method() :
    input = open("rosalind_dna.txt", 'r')
    for line in input :
        return line

def count_nucleotide(input, option) :
    dna_str = input
    dna_str = dna_str.upper()
    count_A = dna_str.count("A")
    count_C = dna_str.count("C")
    count_G = dna_str.count("G")
    count_T = dna_str.count("T")

    if not option :
        print('A, C, G, T :', count_A, count_C, count_G, count_T)
    else :
        for i in range(len(option)) :
            char = option[i]
            if char == "A" :
                print('A', count_A)
            elif char == "C" :
                print('C', count_C)
            elif char == "G" :
                print('G', count_G)
            elif char == "T" :
                print('T', count_T)

input_dna = input_method()
count_nucleotide(input_dna, args.option)