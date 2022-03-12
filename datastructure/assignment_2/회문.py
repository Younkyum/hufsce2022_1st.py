def isPalindrome(x): # 회문 판별
    for i in range(len(x) // 2):
        if x[i] != x[-1-i]:
            return False
    return True

word = input().lower() # 문자열 입력받은 후 소문자 만들기
if isPalindrome(word):
    print("yes")
else:
    print("no")