s="aazzzyyzaaa"
q = ["d","a","y","z"]

arr = [0] * 27

for ch in s :
    arr[ord(ch)-97] += 1
for ch in q:
    index = ord(ch)-97
    print(ch , "=" ,arr[index]) 