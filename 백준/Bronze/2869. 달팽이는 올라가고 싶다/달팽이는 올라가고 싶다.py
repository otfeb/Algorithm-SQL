import math

a,b,v = map(int, input().split())
r = (v-b) / (a-b)
print(math.ceil(r))


