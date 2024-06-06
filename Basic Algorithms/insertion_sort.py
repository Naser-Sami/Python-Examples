
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i

        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        

arr = [2, 6, 5, 1, 3, 4]

insertion_sort(arr)
print(arr)  # [1, 2, 3, 4, 5, 6]
