def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == mid:
        return mid
    elif array[mid]>mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)

N = 5
arr = [-15, -6, 1, 3, 7]

# N = 7
# arr = [-15, -4, 2, 8, 9, 13, 15]

N = 7
arr = [-15, -4, 3, 8, 9, 13, 15]

index = binary_search(arr, 0, N-1)

if index == None:
    print(-1)
else:
    print(index)
