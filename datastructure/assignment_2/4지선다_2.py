def checkScore(answer, score, c_answer): # 점수 확인 함수
    total_score = 0
    for i in range(len(answer)):
        if answer[i] == c_answer[i]:
            total_score += int(score[i])
    return total_score

answer = input().split() # 답안
score = input().split() # 배점
c_member = int(input()) # 인원
idlist = [] # 학번 리스트
scorelist = [] # 점수 리스트
for i in range(c_member):
    iner = input().split()
    idlist.append(iner[0])
    scorelist.append(checkScore(answer, score, iner[1:])) # 학번과 점수 나누기
maxscore = scorelist[0]
for i in scorelist: # 최고점수 확인
    if i > maxscore:
        maxscore = i
print(maxscore)
maxnum = [] # 최고 점수인 학번 리스트
for i in range(len(scorelist)):
    if maxscore == scorelist[i]:
        maxnum.append(idlist[i])
maxnum.sort() # 정렬 후 프린트
for i in maxnum:
    print(i, end=' ')