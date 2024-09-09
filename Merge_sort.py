ls = [2,8,5,3,9,4,1,7]

def merge_sort(ls):

    if len(ls)<=1:
        return ls
    half_ls = len(ls) // 2
    left_part = merge_sort(ls[half_ls:])
    right_part = merge_sort(ls[:half_ls])
    return merge(left_part,right_part)

def merge(left,right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list

print(merge_sort(ls))
print(ls)