from math import *
def isPerfectNum(x):
    total = 1
    for j in range(2, int(sqrt(x)+1)):
        if i % j ==0:
            total += j
            total += int(i / j)
    if total == x:
        return True
    return False

target = int(input())
count = 0
for i in range(2, target + 1):
    if isPerfectNum(i):
        count += 1
print(count)

