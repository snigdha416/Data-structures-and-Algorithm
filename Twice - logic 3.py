size = int(input())
list1 = list(map(int, input().split()))

value = 0
for i in range(size):
    value ^= list1[i]
print(value)
#Time Complexity : O(n)
