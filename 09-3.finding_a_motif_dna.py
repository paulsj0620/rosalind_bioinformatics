#python 2.7 env
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Complementing a Strand of DNA')
    parser.add_argument('-i', '--input', metavar='path', required=False, help='If you want to input your txt file path')
    args = parser.parse_args()

def input_method(path) :
    lines = [line.rstrip('\n') for line in open(path, 'r')]
    return lines

def finding(input_seq) :
    str_s = input_seq[0]
    str_t = input_seq[1]
    switch = 1
    answer_list = []
    cursor = 0
    while switch == 1 :
        index_num = str_s[cursor:].find(str_t)
        if index_num != -1 :
            answer_list.append(str(cursor + index_num + 1))
            cursor += index_num + 1 
        elif index_num == -1 :
            switch = 0
        answer = ' '.join(answer_list)
    print(answer)

seq = input_method(args.input)
finding(seq)