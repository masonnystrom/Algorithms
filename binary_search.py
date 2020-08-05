

def binary_search(arr, target):
    """
    1. compare the target element to the midpoint
        len of array determines midpoint
        the range if we have the left-most index and the right-most index
        midpoint element is floor((right index + left index) / 2)
    2. if the midpoint element matches our target, then we've
        found what we're looking for return the midpoint index
    3. determine which half to go in; toss out the other half
        reassign either left or right index to point to the element psat the midpoint
    4. repeat process: loop this. What's the looping criteria? What tells us that we are done?
        if we see that the low and high are referring to the same index, and the
        element at the index != target, then we can conclude the element isn't in the array
        so we return -1
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        
        mid = (high + low) // 2 # // does floor

        if target == arr[mid]:
            return mid
        
        if target < arr[mid]:
            # cut out the right half and reassign high to mid -1
            high = mid - 1
        if target > arr[mid]:
            # cut left half and reassign low to mid + 1
            low = mid + 1
    # we've reach outside the loop, the element doesn't exist in the array
    return -1

arr = [3, 4, 5, 16, 26, 28, 52, 55]
print(binary_search(arr,58))

