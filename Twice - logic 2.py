size = int(input())
list1 = list(map(int, input().split()))

list1.sort()
i = 0
# 1 1 2 2 3
while i < size - 1:
    if list1[i] == list1[i + 1]:
        i = i + 2
        continue
    break
output = list1[i]
print(output)
#Time Complexity : O(nlog(n))







