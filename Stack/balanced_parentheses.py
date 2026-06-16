s = "(()())"

count = 0

for ch in s:

    if ch == "(":
        count += 1

    else:
        count -= 1

if count == 0:
    print("Balanced")
else:
    print("Not Balanced")