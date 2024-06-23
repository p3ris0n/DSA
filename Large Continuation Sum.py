# large continuation sum.
# Given an array of integers (positive and negative)
# find the largest continuous sum.

import json
import array_list as al  # writing new list to file.

# using kadane's algorithm.

def large_contiguous_sum(arr):
    pointer = 0
    start_index = 0
    end_index = 0
    cur_sum = 0
    max_so_far = arr[0]
    for i in range(len(arr)):
        cur_sum = cur_sum + arr[i]  # current sum equal current array index + current sum.
        if cur_sum > max_so_far:
            max_so_far = cur_sum
            start_index = pointer  # start index at the pointer that gave us the max_so_far.
            end_index = i  # end index at current index (that gave us the max_so_far)
            i += 1
        else:
            if cur_sum < 0:
                cur_sum = 0
                pointer = i + 1  # if current sum falls below zero, pointer is moved 1 step forward.

    print("max-so-far: ", max_so_far)
    print("start_index: ", start_index)
    print("end_index: ", end_index)
    return arr[start_index:end_index + 1]  # splicing, with incursion of the end element itself.


# reading new list from file.
with open("list.json", "r") as file:
    data = json.load(file)

# using new list as array.
arr = data.get(al.list_name, [])
print("max sum of contiguous sum: ", large_contiguous_sum(arr))
