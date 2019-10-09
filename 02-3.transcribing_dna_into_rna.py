import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Counting DNA Nucleotides')
    parser.add_argument('-i', '--input', metavar='input_path', required=True, help='Your input file path')
    args = parser.parse_args()

def input_method(path) :
    input = open(path, 'r' )
    for line in input :
        return line

def transcribe(dna) :
    dna_str = dna.upper()
    rna_str = dna_str.replace("T","U")
    return rna_str

input_dna = input_method(args.input)
print(transcribe(input_dna))