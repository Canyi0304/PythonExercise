num, money = map(int, input().split())

coins = [int(input()) for _ in range(num)]
coins.reverse()

answer = 0
for coin in coins:
    answer += money // coin
    money %= coin
    print(f'coin: {coin}, money: {money}, answer: {answer}')

print(answer)
