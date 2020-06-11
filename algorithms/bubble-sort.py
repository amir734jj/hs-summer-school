def bubble_sort(arr):
    """
    Python program for implementation of Bubble Sort
    """
    n = len(arr)

    for i in range(n):
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                # Swap
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp


# Driver code to test above
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

bubble_sort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),
