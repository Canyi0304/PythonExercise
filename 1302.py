# 입력값 map 선언
lib = dict()

# 입력할 값의 횟수 선언
num = int(input())

# 입력한 책 횟수 만큼 책 출력
for _ in range(num):
    book = input()
    if book in lib:
        lib[book] += 1
    else:
        lib[book] = 1

# map 의 max 값 출력
lib_max = max(lib.values())

# 입력한 dic 값의 key value 출력
can = []
for k, v in lib.items():
    # dic 의 value 와 map 의 max 값 출력
    if v == lib_max:
        can.append(k)
# max 가 같을 경우 sorting

can.sort()
print(can[0])
