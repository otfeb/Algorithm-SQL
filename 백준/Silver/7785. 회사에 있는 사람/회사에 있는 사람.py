import sys
input = sys.stdin.readline

n = int(input())
inCompany = {}

for _ in range(n):
    s = list(input().split())
    if s[1] == "enter":
        inCompany[s[0]] = True
    else:
        del inCompany[s[0]]

print("\n".join(sorted(inCompany.keys(), reverse=True)))