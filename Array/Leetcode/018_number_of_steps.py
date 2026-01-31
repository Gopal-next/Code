def  number_of_steps(num):
    step =0
    while num!=0:
        if num%2 ==0:
            num = num//2
        else:
            num = num -1
        step += 1
    return step

print(number_of_steps(14))
print(number_of_steps(8))