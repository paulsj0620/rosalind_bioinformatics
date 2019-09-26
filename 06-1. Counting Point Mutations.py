input_data = open("rosalind_hamm.txt", 'r')
sample_data = input_data.readlines()

seq_fir = list(sample_data[0][:-1])
seq_sec = list(sample_data[1][:-1])

count = 0
for i in range(len(seq_fir)) :
    if seq_fir[i] != seq_sec[i] :
        count += 1
print(count)
