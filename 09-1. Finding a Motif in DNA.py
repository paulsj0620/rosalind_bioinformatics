input_data = open("rosalind_subs.txt", 'r')
input_seq = input_data.readlines()

str_s = input_seq[0].rstrip()
str_t = input_seq[1].rstrip()
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