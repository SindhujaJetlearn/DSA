def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort_descending(left_half)
    right_half = merge_sort_descending(right_half)
    
    return merge_descending(left_half, right_half)

def merge_descending(left, right):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# Example usage
arr = [12, 45, 2, 78, 56, 23]
sorted_arr = merge_sort_descending(arr)
print(sorted_arr)
