a, b = map(int, input().split())

# 최대공약수 gcd
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

# 최소 공배수
lcm = a*b//gcd(a,b)

print(gcd(a,b))
print(lcm)
