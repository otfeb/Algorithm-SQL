import sys
input = sys.stdin.readline
n, k = map(int, input().split())
items = list(map(int, input().split()))
plug = []
pop = 0
cnt = 0

for i in range(k):
    dist = 0
    pop = 0
    if len(plug) < n and items[i] not in plug:
        plug.append(items[i])
    else:
        if items[i] in plug:
            continue
        else:
            for j in range(len(plug)):
                if plug[j] not in items[i:]:
                    plug.remove(plug[j])
                    cnt += 1
                    plug.append(items[i])
                    break
                else:
                    for x in range(i, len(items)):
                        if plug[j] == items[x]:
                            if dist < x + 1:
                                dist = x + 1
                                pop = j
                                break
                            else:
                                break
            else:
                plug.remove(plug[pop])
                cnt += 1
                plug.append(items[i])
print(cnt)