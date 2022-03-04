def gcd(x, y): # 최대공약수 체크
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y): # 최소공배수 체크
    gcd1 = gcd(x, y)
    return (x*y)//gcd1  # 최소공배수는 최대공약수를 이용해서 확인

s = input().split() # 여러 값 입력받은 후 list 형태로 받음

a = int(s[0])
b = int(s[1])
c = int(s[2])


print(gcd(c, gcd(a, b)), lcm(c, lcm(a, b))) # 세 개의 최대공약수와 최소공배수는 두 개를 먼저 구한 뒤 구하면 된다.