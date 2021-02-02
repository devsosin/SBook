from bisect import bisect_left, bisect_right

N, x = 7, 2
arr = [1,1,2,2,2,2,3]

print(bisect_right(arr, x) - bisect_left(arr, x))