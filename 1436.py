# N 값을 입력 받음
N = int(input())
# 666 초기화
ans = 666
# 비교 숫자 문자열로 작성
answer = '666'

# N이 0이 될때 까지 반복
while N:
    if answer in str(ans):  #만약 '666'이 현재 숫자에 포함되어 있다면
        N = N - 1  # N값 1감소
    ans = ans + 1 # 1이상의 N을 입력 받을 경우 다음 숫자로 넘김

# N번째 나타내는 숫자 출력
print(ans - 1)