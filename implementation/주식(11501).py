import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    stock = list(map(int, input().split()))
    money, max_sell = 0, stock[-1]

    for i in range(n-2, -1, -1):
        if stock[i] < max_sell:
            money += (max_sell - stock[i])
        else:
            max_sell = stock[i]

    print(money)
