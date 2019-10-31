# https://atcoder.jp/contests/abc144/tasks/abc144_e

import math

n,k = map(int, input().split())
lstA = list(map(int, input().split()))
lstF = list(map(int, input().split()))
# n = 11
# k = 14
# lstA = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# lstF = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2]

lstA.sort()
lstF.sort()
lstF.reverse()

def check(x):
    checker = 0
    for i in range(n):
        checker += math.ceil(lstA[i]-x/lstF[i])
    if checker <= k:
        return True
    else:
        return False

left = 0
right = 10**12+1

while left <= right:
    center = (left+right)//2
    if check(center) == True:
        right = center-1
    else:
        left = center+1
    if right==left:
        print(right)
        exit()

# 12
