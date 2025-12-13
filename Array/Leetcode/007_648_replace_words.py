def replacewords(dictt, sentence):
    # sen = sentence.split(' ')
    # dictt.sort(key=len)
    # new_sentence  = ''
    # for i in sen:
    #     k =i
    #     for j in dictt:
    #         l = len(j)
    #         if j == i[:l]:
    #             k  = j
    #             break
            
    #     new_sentence += k + ' '

    # return new_sentence

    root_set = set(dictionary)
    words = sentence.split()
    new_word = []
    for word in words:
        replacee = word
        for i in range(1, len(word)+1):
            p = word[:i]
            if p in root_set:
                replacee = p
                break
        new_word.append(replacee)
    return " ".join(new_word)


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

# dictionary = ["a", "aa", "aaa", "aaaa"]
# sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
# "a a a a a a a a bbb baba a"

# dictionary = ["catt","cat","bat","rat"]
# sentence = "the cattle was rattled by the battery"
# # "the cat was rat by the bat"

# dictionary = ["ac","ab"]
# sentence = "it is abnormal that this solution is accepted"
# "it is ab that this solution is ac"
print(replacewords(dictionary, sentence))