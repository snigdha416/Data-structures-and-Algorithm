size = int(input())
list1 = list(map(int, input().split()))
max1 = list1[0]
for i in range(size):
    if max1 < list1[i]:
        max1 = list1[i]
print(max1)
