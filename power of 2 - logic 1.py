num = int(input())

value = 1
flag = False
for i in range(num):
    if value == num:
        flag = True
        break
    value = value * 2
    if value > num:
        break
print(flag)
