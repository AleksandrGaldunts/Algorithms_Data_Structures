arr = [1,5,9,44,51,61,85,99]
# what index is the number 44 at?
target = 44

start = 0
end = len(arr) - 1
def binary_search_recursive(arr,start,end,target):

    if start>end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid]<target:
        return binary_search_recursive(arr,mid+1,end,target)
    else:
        return binary_search_recursive(arr,start,mid-1,target)

print(binary_search_recursive(arr,start,end,target))


