# 초기값을 음수로 입력해주면 n번째 캐시가 음수가 있는여부를 새로 구한 문제인지 판단
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

count = 0


def f(n):
    global count
    count += 1
    if cache[n] == -1:
        cache[n] = f(n - 1) + f(n - 2)

    return cache[n]

    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # return f(n-1) + f(n-2)


print(f(int(input())))
# print(f'count: {count}')

