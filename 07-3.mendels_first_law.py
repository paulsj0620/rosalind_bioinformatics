#python 2.7 env
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Complementing a Strand of DNA')
    parser.add_argument('-i', '--input', metavar='path', required=False, help='If you want to input your txt file path')
    parser.add_argument('-HD', metavar='Homozygous Dominant', required=False, help='Homozygous Dominant')
    parser.add_argument('-HT', metavar='Heterozygous', required=False, help='Heterozygous')
    parser.add_argument('-HR', metavar='Homozygous Recessive', required=False, help='Homozygous Recessive')
    args = parser.parse_args()

def input_method(path) :
    input = open(path, 'r')
    for line in input :
        return line.split()

def calculate(q_list) :
    k = float(q_list[0]) #Homozygous Dominant
    m = float(q_list[1]) #Heterozygous
    n = float(q_list[2]) #Homozygous Recessive
    HH = (m / (k + m + n)) * ((m-1) / (k + m + n - 1)) * (1.0/4.0)
    HR = (m / (k + m + n)) * (n / (k + m + n - 1)) * (1.0/2.0)
    RH = (n / (k + m + n)) * (m / (k + m + n - 1)) * (1.0/2.0)
    RR = (n / (k + m + n)) * ((n-1) / (k + m + n - 1)) * (1.0)
    print(HH)
    float(HH)
    float(HR)
    float(RR)
    prob = 1 - (HH + HR + RH + RR)
    print('%.5f' % prob)

if not args.input :
    quiz = [args.HD, args.HT, args.HR]
else :
    quiz = input_method(args.input)
calculate(quiz)
