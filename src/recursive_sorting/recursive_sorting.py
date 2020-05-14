# TO-DO: complete the help function below to merge 2 sorted arrays
# 1. divide in half until you have length of 1 (sorted single sub-arrays)
# 2. merge sorted lists together (2 at a time, and compare front of each)


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # for i in range(0, elements + 1):
    #     if arrA[i] > arrB[i]:
    #         merged_arr[i] = arrB[i]
    #         merged_arr[i+1] = arrA[i]
    #     else:
    #         merged_arr[i] = arrA[i]
    #         merged_arr[i+1] = arrB[i]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

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
