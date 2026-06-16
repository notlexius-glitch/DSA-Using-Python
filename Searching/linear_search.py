arr = [10, 20, 30, 40, 50]

x = int(input("Enter number to search: "))

for i in range(len(arr)):
    if arr[i] == x:
        print("Found at index", i)
        break
else:
    print("Not Found")