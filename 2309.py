input_num = [int(input()) for _ in range(9)]
input_num.sort()
tot_num = sum(input_num)


def f():
    for i in range(8):
        for j in range(i+1,9):
            if tot_num - input_num[i] - input_num[j] == 100:
                for k in range(9):
                    if i != k and j != k:
                        print(input_num[k])
                return


f()
