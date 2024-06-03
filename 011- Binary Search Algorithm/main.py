

def binary_search(list, elem, low, high):
    if low > high:
        return None
    else:
        mid = low + (high - low) // 2
        if elem == list[mid]:
            return mid
        elif elem > list[mid]:
            return binary_search(list, elem, mid+1, high)
        else:
            return binary_search(list, elem, low, mid-1)


us_list = [11, 4, 6, 12, 3, 10, 1, 16, 9, 7, 13, 8, 5, 15, 14]
s_list = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
index = binary_search(s_list, 15, 0, len(s_list)-1)
print(index)
