def reverse(arr, start, end):
    while(start < end):
        temp = arr[start]       ##arr[start], arr[end] = arr[end], arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1

arr = [2, 4, 5, 6, 7, 8, 9, 1]
n = len(arr)
d = 3

reverse(arr, 0, d-1)

reverse(arr, d, n-1)

reverse(arr, 0, n-1)

print(arr)
    