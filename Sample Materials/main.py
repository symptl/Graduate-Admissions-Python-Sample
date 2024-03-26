# -----------------------------------------INITIAL SETUP AND DATA IMPORT------------------------------------------------

import sys
import time
import array_algorithms as algorithms
import structures

# Open existing randomized txt of 0 to 100,000 and copy line by line into a list while converting to integers

file = open("Starting Dataset/randomized_list_int.txt", "r")
starting_array = []
for line in file:
    starting_array.append(int(line.strip()))
file.close()

# All code that is to be timed calls "time.perf_counter_ns()"  to gather timestamps and calculate execution time

# -------------------------EXECUTION AND TIMING OF ASSORTED SORTING/ORGANIZATION METHODS--------------------------------
# Run Selection Sort and time the execution
start = time.perf_counter_ns()
sorted_array_1 = algorithms.selection_sort(starting_array)
stop = time.perf_counter_ns()
time_selection_sort = stop - start

# Run Quick Sort and time the execution
start = time.perf_counter_ns()
sorted_array_2 = algorithms.quick_sort(starting_array)
stop = time.perf_counter_ns()
time_quick_sort = stop - start

# Run Merge Sort and time the execution
start = time.perf_counter_ns()
sorted_array_3 = algorithms.merge_sort(starting_array)
stop = time.perf_counter_ns()
time_merge_sort = stop - start

# Copy unsorted starting array into an AVL tree (self-balancing binary search tree)
start = time.perf_counter_ns()
avl_tree = structures.AVLTree()
avl_root = None
for item in starting_array:
    avl_root = avl_tree.insert(avl_root, item)
stop = time.perf_counter_ns()
time_avl_tree = stop - start

# Copy unsorted starting array into an unsorted Linked List (in preparation for testing search methods)
linked_list = structures.LinkedList()
for item in starting_array:
    linked_list.append(item)

# Check that all outputs from array sorting methods are equal (theoretically should be)
# Will flag with a print command if any two are not equal to each other
if sorted_array_1 != sorted_array_2:
    print("Selection Sort does not equal Quick Sort")
if sorted_array_1 != sorted_array_3:
    print("Selection Sort does not equal Merge Sort")
if sorted_array_2 != sorted_array_3:
    print("Quick Sort does not equal Merge Sort")

# --------------------------------EXECUTION AND TIMING OF ASSORTED SEARCH METHODS--------------------------------------
# ALL TEST CASES WILL SEARCH FROM 0 TO 100000 IN INCREMENTS OF 5000 (0, 5000, 10000, ETC.) (21 SEARCHES PER CASE)
# Time Linear Search on the initial unsorted array
start = time.perf_counter_ns()
for i in range(0, 105000, 5000):
    algorithms.linear_search(starting_array, i)
stop = time.perf_counter_ns()
time_linear_search_unsorted = stop - start

# Time Linear Search on the unsorted Linked List
start = time.perf_counter_ns()
for i in range(0, 105000, 5000):
    linked_list.linear_search(i)
stop = time.perf_counter_ns()
time_linear_search_linked_list = stop - start

# Time Linear Search on the same array after sorting
start = time.perf_counter_ns()
for i in range(0, 105000, 5000):
    algorithms.linear_search(sorted_array_1, i)
stop = time.perf_counter_ns()
time_linear_search_sorted = stop - start

# Time Binary Search on sorted array
start = time.perf_counter_ns()
for i in range(0, 105000, 5000):
    algorithms.binary_search(sorted_array_1, i)
stop = time.perf_counter_ns()
time_binary_search_sorted = stop - start

# Time search on AVL Tree (conceptually equivalent to binary search on an array)
start = time.perf_counter_ns()
for i in range(0, 105000, 5000):
    avl_tree.search(avl_root, i)
stop = time.perf_counter_ns()
time_avl_tree_search = stop - start

# ----------------------------------------------VARIABLE SIZE IN MEMORY-------------------------------------------------
# Directly extract sizes of each data structure used to represent an equivalent "dataset"
size_unsorted_array = sys.getsizeof(starting_array)
size_sorted_array = sys.getsizeof(sorted_array_1)

# Utilizes object methods to cycle through all nodes and add up memory sizes
size_avl_tree = avl_tree.inorder_traversal(avl_root)
size_linked_list = linked_list.traverse_list()

# --------------------------------PROCESSING, COMPARISON, AND REPORTING OF RESULTS--------------------------------------
# Convert times from nanoseconds into seconds
time_selection_sort = (time_selection_sort / 1000000000)
time_quick_sort = (time_quick_sort / 1000000000)
time_merge_sort = (time_merge_sort / 1000000000)
time_avl_tree = (time_avl_tree / 1000000000)

time_linear_search_unsorted = (time_linear_search_unsorted / 1000000000)
time_linear_search_linked_list = (time_linear_search_linked_list / 1000000000)
time_linear_search_sorted = (time_linear_search_sorted / 1000000000)
time_binary_search_sorted = (time_binary_search_sorted / 1000000000)
time_avl_tree_search = (time_avl_tree_search / 1000000000)

# Convert variable sizes from bytes to kilobytes
size_unsorted_array = size_unsorted_array / 1000
size_sorted_array = size_sorted_array / 1000
size_avl_tree = size_avl_tree / 1000
size_linked_list = size_linked_list / 1000

# Assemble data into human readable strings
results = (f"Sort Execution Times (seconds)\n"
           f"\n"
           f"Selection Sort execution time: {time_selection_sort:.9f}\n"
           f"Quick Sort execution time: {time_quick_sort:.9f}\n"
           f"Merge Sort execution time: {time_merge_sort:.9f}\n"
           f"AVL Tree creation time: {time_avl_tree:.9f}\n"
           f"\n"
           f"\n"
           f"Search Execution Times (seconds)\n"
           f"\n"
           f"Linear Search (Unsorted Array) execution time: {time_linear_search_unsorted:.9f}\n"
           f"Linear Search (Linked List, unsorted) execution time: {time_linear_search_linked_list:.9f}\n"
           f"Linear Search (Sorted Array) execution time: {time_linear_search_sorted:.9f}\n"
           f"Binary Search (Sorted Array) execution time: {time_binary_search_sorted:.9f}\n"
           f"AVL Tree Search (Binary equivalent) execution time: {time_avl_tree_search:.9f}\n"
           f"\n"
           f"\n"
           f"Variable Sizes of Different Data Structures (kilobytes)\n"
           f"\n"
           f"Unsorted Array Size: {size_unsorted_array}\n"
           f"Sorted Array Size: {size_sorted_array}\n"
           f"AVL Tree Size: {size_avl_tree}\n"
           f"Linked List Size: {size_linked_list}\n")


# Output results into specified text file
file = open("Results/results.txt", "w")
file.write(results)
file.close()


