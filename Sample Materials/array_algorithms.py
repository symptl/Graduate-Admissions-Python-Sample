# Implementation of all algorithms in this demo
# Big O notation is included for each, next to the titles

# LINEAR SEARCH - O(n)
# Return index of first instance of search value
def linear_search(array, value):
    for index, item in enumerate(array):
        if item == value:
            return index
    return None


# BINARY SEARCH - O(log(n)
# Return index of first instance of search value
# Guesses midpoint of remaining terms and picks lesser or greater half as appropriate to halve window until value found.
# Requires array to be sorted in ascending order

def binary_search(array, value):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = array[middle]
        if guess == value:
            return middle
        elif guess > value:
            high = middle - 1
        else:
            low = middle + 1
    return None


# SELECTION SORT - O(n^2)
# Return array sorted in ascending order
# Goes through unsorted portion of array and finds min value, swaps with current value,
# then increments by 1 and repeats until entire array is sorted. (relatively slow)
def selection_sort(array):
    internal_array = array[:]

    for i in range(len(internal_array)):
        min_idx = i
        for j in range(i + 1, len(internal_array)):
            if internal_array[j] < internal_array[min_idx]:
                min_idx = j

        internal_array[i], internal_array[min_idx] = internal_array[min_idx], internal_array[i]

    return internal_array


# QUICK SORT - O(n*log(n))
# Return array sorted in ascending order (faster than selection sort)
# Sorts values in an array relative to a pivot value (less than or greater than)
# Recursively calls itself on any sub-array with 2 or more elements until entire array is sorted
def quick_sort(array):
    # Base case: An array with one or no elements is already "sorted"
    if len(array) <= 1:
        return array

    # Recursive case: Sort larger arrays around a pivot, and quick sort each sub-array
    else:
        pivot = array[0]
        lower = [value for value in array[1:] if value <= pivot]
        greater = [value for value in array[1:] if value > pivot]
        return quick_sort(lower) + [pivot] + quick_sort(greater)


# MERGE SORT - O(n*(log(n))
# Return array sorted in ascending order (theoretically same order of magnitude as quick sort)
# Breaks down array to single elements
# Merges elements from two smaller arrays in ascending order
# Faster than selection sort because entire array doesn't need to be scanned during merging, due to it being sorted

def merge_sort(array):
    # Base case: An array with one or no elements is already "sorted"
    if len(array) <= 1:
        return array

    # Recursive case: split the array into halves and call merge sort on each sub-array
    else:
        mid = len(array) // 2
        left_array = merge_sort(array[:mid])
        right_array = merge_sort(array[mid:])

        return merge(left_array, right_array)


def merge(left, right):
    sorted_array = []
    left_index = 0
    right_index = 0

    # Compare each element of the left and right array and add the smaller value to the sorted array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # If there are remaining elements in left or right, add them to the sorted array
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array
