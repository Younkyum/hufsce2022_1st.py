def isPalindrome(x): # 회문 판멸
    for i in range(len(x) // 2):
        if x[i] != x[-1-i]:
            return False
    return True

word = input().lower() # 문자열 소문자로 변환
palindrome = [] # 회문들을 모을 리스트
for i in range(len(word)): # 부문자열 모두 확인
    for j in range(len(word) - i):
        if len(word[i:i+j+1]) != 1 and isPalindrome(word[i:i+j+1]):
            palindrome.append(word[i:i+j+1])
palindrome.sort() # 정렬
if len(palindrome) != 0: # 부문자열 중 회문이 없을 경우를 제외
    maxlen = len(palindrome[0])
    for i in palindrome:
        if maxlen < len(i):
            maxlen = len(i)
    for i in palindrome:
        if len(i) == maxlen: # 최대 길이의 부회문만 출력
            print(i, end=' ')
