arr = [1,2,2,3,1,4]

freq = {}

for i in arr:
    freq[i] = freq.get(i,0) + 1

print(freq)