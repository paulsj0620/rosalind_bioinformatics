import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Complementing a Strand of DNA')
    parser.add_argument('-i', '--input', metavar='path', required=False, help='If you want to input your txt file path')
    parser.add_argument('-m', '--month', metavar='month', type=int, required=False, help='month that you want to know about')
    parser.add_argument('-l', '--litter', metavar='litter', type=int, required=False, help='litter that you want to know about')
    args = parser.parse_args()

def input_method(path) :
    input = open(path, 'r' )
    for line in input :
        return line

def input_data(file) :
    file = file.split()
    input_month = int(file[0])
    input_litter = int(file[1])
    return input_month, input_litter

def set_number(num) :
    input_month = num[0] 
    input_litter = num[1]
    print(input_month)
    print(input_litter)
    rab = 1
    rab_n = 1
    month = 2
    while month < input_month :
        if month % 2 == 1 : 
            rab = rab * input_litter
            rab = rab + rab_n
            month += 1
        elif month % 2 != 1 :
            rab_n = rab_n * input_litter
            rab_n = rab + rab_n
            month += 1
    if month == input_month :
        if rab < rab_n : 
            print(rab_n)
        else :
            print(rab)

if not args.input :
    number = (args.month, args.litter) 
    set_number(number)
else : 
    file = input_method(args.input)
    set_number(input_data(file))