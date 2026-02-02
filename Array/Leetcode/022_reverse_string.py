def reversee(s):
    li = []
    for i in range(len(s)-1,-1,-1):
        li.append(s[i])
    return li
    
    # two pointer
    
print(reversee(["h","e","l","l","o"]))
print(reversee(["H","a","n","n","a","h"]))