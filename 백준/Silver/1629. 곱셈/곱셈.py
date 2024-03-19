import sys
input = sys.stdin.readline

def power(a, b, c):
    if b == 0:
        return 1
    
    half_power = power(a, b//2, c)

    if b % 2 == 0:
        return (half_power%c * half_power%c) % c
    else:
        return (half_power%c * half_power%c * a%c) % c

a,b,c = map(int, input().split())
print(power(a,b,c))