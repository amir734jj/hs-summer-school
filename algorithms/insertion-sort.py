def insertion_sort(arr):
    """
    Python program for implementation of Insertion Sort
    """

    n = len(arr)

    for i in range(1, n):
        item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = item


# Driver code to test above
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

insertion_sort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),
