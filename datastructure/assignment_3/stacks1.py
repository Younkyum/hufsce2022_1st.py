def check_bracket(words):  # 괄호의 짝을 파악하는 함수
    bl = ['(', '{', '[']  # 여는 괄호
    bu = [')', '}', ']']  # 닫는 괄호
    stack = []  # 괄호를 받는 Stack
    for i in range(len(words)):  # 한 글자씩 파악
        if words[i] in bl:
            stack.append(words[i])  # Stack 괄호 append
        if words[i] in bu:
            if len(stack) == 0:  # Stack 내부 괄호 없을 경우 오류 리턴
                return False
            popped = stack.pop()  # Stack pop
            if popped != bl[bu.index(words[i])]:  # 다른 경우 오류 리턴
                return False
    if len(stack) != 0:  # Stack 요소가 남으면 오류 리턴
        return False
    return True


word = input()
if check_bracket(word):
    print(1)
else:
    print(0)
