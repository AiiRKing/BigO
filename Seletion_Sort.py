def selectionSort(array, size):

    for min in range(size):
        min_index = min

        for j in range(min + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[min], array[min_index]) = (array[min_index], array[min])

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending order by selection sort is: ')
print(arr)