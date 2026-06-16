arr = [10, 20, 30, 40, 50]

x = int(input("Enter number: "))

low = 0
high = len(arr)-1

while low <= high:

    mid = (low + high)//2

    if arr[mid] == x:
        print("Found at index", mid)
        break

    elif arr[mid] < x:
        low = mid + 1

    else:
        high = mid - 1