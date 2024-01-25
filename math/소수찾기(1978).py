n = int(input())
numbers = map(int, input().split())

def is_prime(number):
    if number == 1:
        return False # 1은 소수가 아님
    
    for i in range(2, int(number**(1/2))+1):
        if number % i == 0:
            return False # 소수가 아님
    return True # 소수임

cnt = 0
for number in numbers:
    if is_prime(number):
        cnt += 1

print(cnt)
