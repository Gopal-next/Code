def totalMoney(n):
    count = 0
    i = 1
    w =1
    for day in range(1,n+1):
        count += i
        i += 1
        if day%7==0:
            w +=1
            i = w
    return count

print(totalMoney(4))
print(totalMoney(10))
print(totalMoney(20))
