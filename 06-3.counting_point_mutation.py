import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Counting Point Mutations')
    parser.add_argument('-i', '--input', metavar='path', required=False, help='If you want to input your txt file path')
    args = parser.parse_args()

lines = []
def input_method(path) :
    input_data = open(path, 'r')
    for line in input_data :
        lines.append(line)
def point_mutation(sample_data) :
    seq_fir = list(sample_data[0][:-1])
    seq_sec = list(sample_data[1][:-1])
    count = 0
    for i in range(len(seq_fir)) :
        if seq_fir[i] != seq_sec[i] :
            count += 1
    print(count)

input_method(args.input)
point_mutation(lines)
