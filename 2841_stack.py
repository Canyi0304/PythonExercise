import sys

# 입력이 50만이 있을수 있어서 sys.stdin.readline() 사용
input_str = sys.stdin.readline
N, P = map(int, input_str().split())

# index가 1-6까지이므로 배열 7 만들기
stack = [[] for _ in range(7)]

# 손가락 움직이는 횟수: ans
ans = 0

for _ in range(N):
    # 줄 라인 입력
    line, p = map(int, input_str().split())
    # stack의 값이 있거나 stack 최상단의 값이 p보다 클경우
    while stack[line] and stack[line][-1] > p:
        # stack에서 값을 뺀다.
        stack[line].pop()
        # stack에서 값을 뺄때 손까락도 같이 움직인다.
        ans += 1

    # 라인이 비어있지 않고 상단값이 p와 같을 경우 무시
    if stack[line] and stack[line][-1] == p:
        continue

    # 그렇지 않을 경우 stack에 p를 넣어줌
    stack[line].append(p)
    # 손가락도 같이 움직임
    ans += 1
    # 중간값 출력
    # print(stack[line], ans)


print(ans)
