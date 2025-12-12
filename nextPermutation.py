def nextPermutation(arr):
    n = len(arr)

    # 1. Find pivot
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break

    # If no pivot, array is highest permutation → reverse to smallest
    if pivot == -1:
        arr.reverse()
        return arr

    # 2. Find the next greater element from right
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # 3. Reverse the part after pivot
    arr[pivot + 1:] = reversed(arr[pivot + 1:])

    return arr


# Example
arr = [2, 4, 5, 9, 8, 7]
print(nextPermutation(arr))   # Output: [2, 4, 7, 5, 8, 9]
