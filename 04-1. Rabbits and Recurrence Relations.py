input = open("rosalind_fib.txt", 'r')
question = str(input.readline())
question.rstrip('\n')
number = question.split()
input_month = int(number[0])
input_litter = int(number[1])
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
