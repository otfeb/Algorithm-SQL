n = int(input())
k = int(input())
arr = []
result = []

for i in range(n):
    s = input()
    arr.append(s)

if k == 2:
    for i in range(n):
        for j in range(n):
            if i != j:
                result.append(arr[i]+arr[j])

elif k == 3:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j != k != i:
                    result.append(arr[i]+arr[j]+arr[k])

else:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for a in range(n):
                    if i != j != k != a != i != k and a != j :
                        result.append(arr[i]+arr[j]+arr[k]+arr[a])

print(len(set(result)))
