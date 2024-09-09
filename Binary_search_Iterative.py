def binary_search_iterative(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

arr = [1, 5, 9, 44, 51, 61, 85, 99]
target = 44

print(binary_search_iterative(arr, target))

