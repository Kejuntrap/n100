str = "I am an NLPer"
bigram1 = []
for i in range(len(str) - 1):
    bigram1.append(str[i:i + 2])
print(bigram1)

tango = str.split()
bigram2 = []
for i in range(len(tango) - 1):
    bigram2.append(tango[i] + tango[i + 1])
print(bigram2)
