size = int(input())
list1 = list(map(int, input().split()))
key = int(input())

print(list1.count(key))

count = 0
for i in range(size):
    if key == list1[i]:
        count += 1
print(count)

