arr = [5, 3, 8, 1, 2]

for i in range(len(arr)):
    for j in range(len(arr)-1-i):

        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)