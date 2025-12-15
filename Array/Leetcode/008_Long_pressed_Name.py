def long_pressed(name, typed):
    i = j = 0

    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j-1]:
            j += 1
        else:
            return False
    return i == len(name)
    

name = "aleex"
typed = "aaleex"

print(long_pressed(name, typed))

n = "saeed"

t = "ssaaedd"
print(long_pressed(n,t))