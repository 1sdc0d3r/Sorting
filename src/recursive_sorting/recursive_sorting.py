# TO-DO: complete the help function below to merge 2 sorted arrays
# 1. divide in half until you have length of 1 (sorted single sub-arrays)
# 2. merge sorted lists together (2 at a time, and compare front of each)


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    x, y, z = 0, 0, 0

    while(x < len(arrA) and y < len(arrB)):
        if(arrA[x] < arrB[y]):
            merged_arr[z] = arrA[x]
            x += 1
        else:
            merged_arr[z] = arrB[y]
            y += 1
        z += 1

    if(x < len(arrA)):
        while(z < len(merged_arr)):
            merged_arr[z] = arrA[x]
            z += 1
            x += 1

    if(y < len(arrB)):
        while(z < len(merged_arr)):
            merged_arr[z] = arrB[y]
            z += 1
            y += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if(len(arr) <= 1):
        return arr
    else:
        half = len(arr) // 2
        arr1 = arr[half:]
        arr2 = arr[:half]

        left = merge_sort(arr1)
        right = merge_sort(arr2)

        return merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


arr1 = [2, 7, 2, 5, 8, 1, 0, 3, 8]
arr2 = [9, 7, 3, 9, 2, 7, 0, 0, 5]
print(merge(arr1, arr2))
