import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

ans = 0
def check(t_str):
    global ans
    if len(s) == len(t_str):
        if s == t_str:
            ans = 1
        return 
    
    if t_str[-1] == 'A':
        check(t_str[:-1])

    if t_str[0] == 'B':
        check(t_str[1:][::-1])

check(t)
print(ans)
