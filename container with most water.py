size = int(input())
list1 = list(map(int, input().split()))

maxArea = 0
for i in range(size):
    for j in range(i + 1, size):
        area = min(list1[i], list1[j]) * (j - i)
        if maxArea < area: maxArea = area

print(maxArea)
