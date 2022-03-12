answer = input().split()
score = input().split()
c_answer = input().split()

total_score = 0

for i in range(len(answer)): # 답이 맞을 때 맞는 배점 추가
    if answer[i] == c_answer[i]:
        total_score += int(score[i])

print(total_score)