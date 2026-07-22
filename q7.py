s = "hello"

for ch in s:
    pos = ord(ch.lower())-ord("a")+1
    print(ch,"->",pos)

