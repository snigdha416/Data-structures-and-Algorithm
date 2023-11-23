size = int(input())
list1 = list(map(int, input().split()))
target = int(input())

flag = 0
for i in range(size):
    for j in range(i + 1, size):
        if list1[i] + list1[j] == target:
            flag = 1
            print(list1[i], list1[j])
            break
    if flag == 1: break
#Time Complexity : O(n^2)
