input_data = open("rosalind_iprb.txt", 'r')
inte = input_data.readlines()
quiz = inte[0].split()

k = int(quiz[0]) #Homozygous Dominant
m = int(quiz[1]) #Heterozygous
n = int(quiz[2]) #Homozygous Recessive

HH = (m / (k + m + n)) * ((m-1) / (k + m + n - 1)) * (1 /4)
HR = (m / (k + m + n)) * (n / (k + m + n - 1)) * (1 /2)
RH = (n / (k + m + n)) * (m / (k + m + n - 1)) * (1 /2)
RR = (n / (k + m + n)) * ((n-1) / (k + m + n - 1)) * (1)

float(HH)
float(HR)
float(RR)
prob = 1 - (HH + HR + RH + RR)
print('%.5f' % prob)