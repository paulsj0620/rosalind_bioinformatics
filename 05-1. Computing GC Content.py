input_data = open("rosalind_gc.txt", 'r')
sample_data = input_data.readlines()
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
            header.append(sample_data[k][:-1])
        elif index_s[j] < k < index_e[j] :
            temp.append(sample_data[k][:-1])
    temp_seq = "".join(temp)
    seq.append(temp_seq)

count = []

for l in range(len(seq)) :
    total = len(seq[l])
    count_c = seq[l].count('C')
    count_g = seq[l].count('G')
    value = ((count_c + count_g) / total) * 100
    count.append(value)
max_value = max(count)
m = count.index(max_value)
num = format(max_value, ".6f")
print(header[m][1:])
print(num)
