s1 = input("First string: ")
s2 = input("Second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")