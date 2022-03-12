def isAnswer(answer, iner): # 답인지 확인
    if answer == iner:
        return True
    return False

answer = input().split() # 답안
score = input().split() # 배점
c_member = int(input()) # 인원
scored = [] # 맞은 사람 수 리스트
for i in answer:
    scored.append(0)
for i in range(c_member):
    member = input().split()
    for j in range(len(member) - 1):
        if isAnswer(answer[j], member[j+1]): # 맞은 경우 그 위치에 한명 추가
            scored[j] += 1
smallest = scored[0]
for i in scored:
    if smallest > i: # 맞은 사람 최소값 구하기
        smallest = i
print((smallest/c_member) * 100) # 최소 정답률 출력
check = 0
for i in scored: # 최소 정답률인 문제들 번호 출력
    check += 1
    if smallest == i:
        print(check, end=' ')
