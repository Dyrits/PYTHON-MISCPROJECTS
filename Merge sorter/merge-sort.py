def merge_sort(items):
    if len(items) < 2:
        return items
    middle_index = len(items) / 2
    left_sorted = merge_sort(items[middle_index:])
    right_sorted = merge_sort(items[:middle_index])
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    while (left and right):
        result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    result.extend(left or right)
    return result
