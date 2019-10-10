import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Computing GC Content')
    parser.add_argument('-i', '--input', metavar='path', required=False, help='If you want to input your txt file path')
    args = parser.parse_args()

def input_method(path) :
    lines = [line.rstrip('\n') for line in open(path, 'r')]
    return lines

def sort_fastq(sample_data) :
    index_s = []
    index_e = []
    header = []
    seq = []
    for i in sample_data :
        if '>' in i :
            index_s.append(sample_data.index(i))
    index_e = index_s[1:]
    index_e.append(len(sample_data)+1)
    for j in range(len(index_s)) :
        temp = []
        for k in range(len(sample_data)) :
            if k == index_s[j] :
                header.append(sample_data[k])
            elif index_s[j] < k < index_e[j] :
                temp.append(sample_data[k])
        temp_seq = "".join(temp)
        seq.append(temp_seq)
    return seq, header

def count_gc(seq, header) :
    count = []
    for l in range(len(seq)) :
        total = float(len(seq[l]))
        count_c = float(seq[l].count('C'))
        count_g = float(seq[l].count('G'))
        value = ((count_c + count_g) / total) * 100
        count.append(value)
    max_value = max(count)
    m = count.index(max_value)
    print(m)
    num = format(max_value, ".6f")
    print(header[m][1:])
    print(num)

sample_data = input_method(args.input)
seq_and_header = list(sort_fastq(sample_data))
count_gc(seq_and_header[0], seq_and_header[1])
