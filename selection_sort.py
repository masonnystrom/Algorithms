def selection_sort(arr):
    """
    iterate through the array (represents sorted-unsorted boundary and move across array)
    
    iterate through the array, finding the smallest element
    in the unsorted portion of the array
    once that's found, swap it iwth the element on the right edge
    of the sorted-unsorted boundary
    """
    for i in range(len(arr)):
        boundary = i
        
        smallest_value = arr[boundary]
        smallest_index = boundary

        for unsorted_index in range(boundary, len(arr)):
           if arr[unsorted_index] < smallest_value:
               smallest_value = arr[unsorted_index]
               smallest_index = unsorted_index

        # smallest_index is the index of the smallest element in the unsorted portion

        arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]
    return arr

arr = [5, 55, 6, 67, 16, 9, 25, 43, 16]
print(selection_sort(arr))
