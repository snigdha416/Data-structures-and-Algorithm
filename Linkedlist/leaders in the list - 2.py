size = int(input())
list1 = list(map(int, input().split()))
max1 = list1[size - 1]
leaders = [max1]
for i in range(size - 2, -1, -1):
    if max1 < list1[i]:
        max1 = list1[i]
        leaders.append(max1)
leaders.reverse()
print(leaders)
