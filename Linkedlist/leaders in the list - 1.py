size = int(input())
list1 = list(map(int, input().split()))
leaders = []
for i in range(size - 1):
    max1 = list1[i + 1]
    for j in range(i + 1, size):
        if max1 < list1[j]: max1 = list1[j]
    if list1[i] > max1: leaders.append(list1[i])
leaders.append(list1[size - 1])
print(leaders)
