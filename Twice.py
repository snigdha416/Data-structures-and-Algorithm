size = int(input())
list1 = list(map(int, input().split()))

output = None

for i in range(size):
    count = 0
    for j in range(size):
        if list1[i] == list1[j]: count += 1
    if count == 1:
        output = list1[i]
        break

print(output)

# 5
# 1 2 3 2 1
#             i
# 1 1 2 2 3
#            i
# 1 1 7 7 9
# 1 2 2 3 3
output = None
list1.sort()
i = 0
while i < size - 1:
    if list1[i] == list1[i + 1]:
        i = i + 2
        continue
    else:
        output = list1[i]
        break

if i == size - 1: output = list1[i]
print(output)








