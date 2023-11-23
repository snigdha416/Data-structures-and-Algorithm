# size -> 5
# elements -> 1 2 3 4 5

size = int(input())
list1 = list(map(int, input().split()))

'''for i in range(size):
    list1.append(int(input()))'''

for i in range(size):
    print(list1[i], end = " ")

for i in list1:
    print(i, sep = " ")
