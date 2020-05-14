# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        for j in range(smallest_index+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for j in range(0, len(arr) - 1):
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # bubble_sort(arr)
    return arr
# for i in range(0, len(arr) - 1):
    # if arr[i] > arr[i+1]:
    # arr[i], arr[i+1] = arr[i+1], arr[i]
    # bubble_sort(arr)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


test_array = [1, 3, 8, 2, 5, 0, 9, 2, 4]

print(bubble_sort(test_array))
