def baseball(operations):
    res = []

    for i in range(len(operations)):
        if operations[i].lstrip('-').isdigit():
            res.append(int(operations[i]))
        elif operations[i] == "+":
            res.append(res[-1]+res[-2])
        elif operations[i] == "D":
            res.append(res[-1]*2)
        else:
            res.remove(res[-1])
    return sum(res)

    pass

ops = ["5","2","C","D","+"]
print(baseball(ops))

opss = ["5","-2","4","C","D","9","+","+"]
print(baseball(opss))
o = ["1","C"]
# print(baseball(o))
