def isValid(s):
    # dictt = {')':'(' , '}':'{' ,']':'['}

    # stack = []
    # for i in s:
    #     if i in dictt:
    #         if stack and stack[-1] == dictt[i]:
    #             stack.pop()
    #         else:
    #             return False
    #     else:
    #         stack.append(i)
    # return len(stack)  ==0


    stack = []

    for ch in s:
        if ch == '(' or ch == "{" or ch == "[":
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            print(top)
            if ch == ')' and top != '(':
                return False
            if ch == ']' and top != '[':
                return False
            if ch == '}' and top != '{':
                return False
    return len(stack) ==0

s = "()"
print(isValid(s))