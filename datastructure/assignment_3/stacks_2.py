def check_bracket(words):  # 괄호 확인
    bl = ['(', '{', '[']  # 여는 괄호
    bu = [')', '}', ']']  # 닫는 괄호
    stack = []  # 괄호를 받는 Stack
    stack_index = []  # 괄호의 위치를 저장하는 Stack
    for i in range(len(words)):  # 글자 하나씩 파악
        if words[i] in bl:
            stack.append(words[i])  # Stack 괄호 append
            stack_index.append(i)  # 위치도 함께 append
        if words[i] in bu:
            if len(stack) == 0:  # Stack 내부에 괄호가 없을 경우 오류 리턴
                return i, words[i]
            popped = stack.pop()  # Stack pop
            stack_index.pop()  # Stack 위치 pop
            if popped != bl[bu.index(words[i])]:  # 오류 리턴
                return i, words[i]
    if len(stack) != 0:
        return stack_index[-1], stack[-1]  # 남은경우 Stack 마지막(-1) 위치와 함께 리
    return -1, None


word = input()
index, error_word = check_bracket(word)
if index == -1:
    print(1)
else:  # 에러 종류와 위치를 출력
    print(index, end=' ')
    if error_word == ')':
        print("error1")
    elif error_word == '}':
        print("error2")
    elif error_word == ']':
        print("error3")
    elif error_word == '(':
        print("error4")
    elif error_word == '{':
        print("error5")
    elif error_word == '[':
        print("error6")
