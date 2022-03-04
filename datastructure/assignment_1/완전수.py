from math import *
target = int(input())
count = 0
for i in range(2, target + 1):
    total = 1 # 1은 항상 약수임
    for j in range(2, int(sqrt(i)+1)):
        if i % j == 0: # 나머지가 0이면 약수
            total += j
            total += int(i / j)
    if total == i: # 모두 더하므로 다 합하면 2배
        count = count + 1
print(count)
