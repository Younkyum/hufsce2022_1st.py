def print_error(bracket, position, line_num):  # 에러 종류와 위치를 출력해주는 함수
    if bracket == ')':
        print('error1: {0} at position {1} in line {2}'.format(bracket, position, line_num))
    elif bracket == '}':
        print('error2: {0} at position {1} in line {2}'.format(bracket, position, line_num))
    elif bracket == ']':
        print('error3: {0} at position {1} in line {2}'.format(bracket, position, line_num))
    elif bracket == '(':
        print('error4: {0} at position {1} in line {2}'.format(bracket, position, line_num))
    elif bracket == '{':
        print('error5: {0} at position {1} in line {2}'.format(bracket, position, line_num))
    elif bracket == '[':
        print('error6: {0} at position {1} in line {2}'.format(bracket, position, line_num))


def check_bracket(strings):  # 괄호의 짝을 파악하는 함수
    bl = ['(', '{', '[']  # 여는 괄호
    bu = [')', '}', ']']  # 닫는 괄호
    stack = []  # 괄호를 받는 Stack
    stack_index = []  # 괄호의 위치를 저장하는 Stack
    line_counter = 0  # 줄
    for line in strings:  # 한 줄씩 파악
        line_counter += 1
        for i in range(len(line)):
            if line[i] in bl:  # 여는 괄호 확인
                stack.append(line[i])  # Stack 괄호 append
                stack_index.append([i, line_counter])  # 위치도 함께 append
            if line[i] in bu:  # 닫는 괄호 확인
                if len(stack) == 0:  # Stack 내부에 괄호가 없을 경우 오류 리턴
                    return line[i], i, line_counter
                popped = stack.pop()  # Stack pop
                stack_index.pop()  # Stack 위치 pop
                if popped != bl[bu.index(line[i])]:  # 오류 리턴
                    return line[i], i, line_counter
    if len(stack) != 0:
        return stack[-1], stack_index[-1][0], stack_index[-1][1]  # 남은경우 Stack 마지막(-1) 위치와 함께 리턴
    else:
        return False, 0, 0


lines = []
while True:
    try:  # EOF 입력받음
        inline = input()
        lines.append(inline)
    except EOFError:
        break
a, b, c = check_bracket(lines)
if not a:
    print(1)
else:
    print_error(a, b + 1, c)
