def linear_search(arr, target):
    for elem in arr:
        if elem == target:
            return True
    return False

def binary_search(arr, target):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

accounts = [101, 205, 302, 450, 101, 500]
target = 205

print("Linear Search:", linear_search(accounts, target))
print("Binary Search:", binary_search(accounts, target))
