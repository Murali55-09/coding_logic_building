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
 



 ## Works only on lists
# ✔ Reverses the list in place (modifies the original list)
# ✔ Returns None


# ✔ Works on any iterable (list, tuple, string, etc.)
# ✔ Does NOT modify the original object
# ✔ Returns an iterator (not a list)
# ✔ Must be converted to a list or assigned using slicing

# arr = [1, 2, 3]
# x = reversed(arr)

# print(list(x))  # [3, 2, 1]
# print(arr) 
# print(list(x)) --> gives []  Because x = reversed(arr) creates an iterator, and an iterator can be used only once.
# print(x) --> gives error This is because x is an iterator, not a list.