import sys

Num = int(input())

for _ in range(Num):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
