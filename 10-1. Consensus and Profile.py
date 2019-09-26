input_file = open("rosalind_cons.txt", 'r')
input_data = input_file.readlines()
index_s = []
index_e = []
header = []
seq = []

for i in input_data :
    if '>' in i :
        index_s.append(input_data.index(i))
index_e = index_s[1:]
index_e.append(len(input_data)+1)

for j in range(len(index_s)) :
    temp = []
    for k in range(len(input_data)) :
        if k == index_s[j] :
            header.append(input_data[k][:-1])
        elif index_s[j] < k < index_e[j] :
            temp.append(input_data[k][:-1])
    temp_seq = "".join(temp)
    seq.append(temp_seq)

list_a = []
list_c = []
list_g = []
list_t = []

for i in range(len(seq)) :
    if i == 1 :
        for j in range(len(seq[i])) :
            list_a.append(0)
            list_c.append(0)
            list_g.append(0)
            list_t.append(0)

for k in range(len(seq)) :
    con_seq = seq[k]
    for s in range(len(con_seq)) :
        if con_seq[s] == 'A' :
            count_a = 0
            count_a += 1
            list_a[s] += count_a 
        elif con_seq[s] == 'C' :
            count_c = 0
            count_c += 1
            list_c[s] += count_c
        elif con_seq[s] == 'G' :
            count_g = 0
            count_g += 1
            list_g[s] += count_g
        elif con_seq[s] == 'T' :
            count_t = 0
            count_t += 1
            list_t[s] += count_t
result = []

for l in range(len(list_a)) :
    temp_a = list_a[l]
    temp_c = list_c[l]
    temp_g = list_g[l]
    temp_t = list_t[l]
    max_seq = max([temp_a, temp_c, temp_g, temp_t]) 
    if max_seq == temp_a :
        result.append('A')
    elif max_seq == temp_c :
        result.append('C')
    elif max_seq == temp_g :
        result.append('G')
    elif max_seq == temp_t :
        result.append('T')

list_a = list(map(str, list_a))
list_c = list(map(str, list_c))
list_g = list(map(str, list_g))
list_t = list(map(str, list_t))

print("".join(result))
join_a = " ".join(list_a)
join_c = " ".join(list_c)
join_g = " ".join(list_g)
join_t = " ".join(list_t)
print("A: " + join_a)
print("C: " + join_c)
print("G: " + join_g)
print("T: " + join_t)