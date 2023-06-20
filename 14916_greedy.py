import sys

# input 성능 개선
input = sys.stdin.readline
N = int(input())

# 5 거스름 변수 선언
tmp = N % 5

if N == 1 or N == 3 or N <= 0:
    print(-1)
    # N이 5로 나눴을때 답이 짝수일 경우 2를 나눈 횟수를 더함
elif tmp % 2 == 0:
    print((N //5 ) + (tmp // 2))
    # N이 5로 나눴을때 답이 홀수일 경우 2를 나눈 횟수를 더함
else:
    print((N // 5 - 1) + ((tmp -5) // 2))


