def isPowerOfTwo(num):
    while num > 1:
        if num % 2 == 1: return False
        num = num // 2
    return True

num = int(input())
print(isPowerOfTwo(num))

#Time Complexity : log2(n)
