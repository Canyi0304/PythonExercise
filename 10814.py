import sys

# input 성능 개선
input = sys.stdin.readline
# 회원 수 정수로 입력
N = int(input())

# 회원 정보 저장할 리스트 생성
M = []

# 회원정보 입력

for _ in range(N):
    age, name = input().split()
    M.append((int(age), name))

    # print(age, name)

# 나이 순으로 회원 정렬 (lamda: 익명 함수 지정, a: 각 맴버를 나타 내는 매개 변수, a[0]: 해당 매개 변수인 나이)
M.sort(key=lambda a: a[0])

# 정렬된 회원 정보 출력
for member in M:
    print(member[0], member[1])
