def jewels_stones(jewel, stones):
    # c = 0
    # for i in stones:
    #     if i in jewel:
    #         c += 1
    # return c


    # other
    j = {}

    for ch in jewel:
        j[ch] = 1

    count = 0
    for ch in stones:
        if ch in j:
            count += 1
    return count
jewel = "aA"
stones = "aAAbbbb"
print(jewels_stones(jewel, stones))