size = int(input())
list1 = list(map(int, input().split()))
key = int(input())

#print(key in list1)
#print(list1.count(key) > 0)

flag = False
for i in range(size):
    if key == list1[i]:
        flag = True
        break
print(flag)

