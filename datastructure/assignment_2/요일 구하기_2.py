def isleapyear(x): # 윤년인지 확인
    if ((x % 4 == 0 and x % 100 != 0) or x % 400 == 0):
        return True
    return False

def datecounter(x, y): # 날짜의 차이 확인
    total = 0
    for i in range(x, y):
        total += 365
        if isleapyear(i):
            total += 1
    return total

date = ["월", "화", "수", "목", "금", "토", "일"] # 요일을 파악하기 위해 list로 정리
come = input().split()
day = input()
x = int(come[0])
y = int(come[1])
daydiff = datecounter(x, y) # 날짜 차이
target = date.index(day) # 요일 index 확인
print(date[(target + daydiff) % 7]) # 날짜차이와 index를 더해 7로 나누면 해당 요일 프