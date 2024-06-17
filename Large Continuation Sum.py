# large continuation sum.
# Given an array of integers (positive and negative)
# find the largest continuous sum.

# using kadane's algorithm.
def large_contiguous_sum(arr):
    pointer = 0
    start_index = 0
    end_index = 0
    cur_sum = 0
    max_so_far = arr[0]
    for i in range(len(arr)):
        cur_sum = cur_sum + arr[i]
        if cur_sum > max_so_far:
            max_so_far = cur_sum
            start_index = pointer
            end_index = i
            i += 1
        else:
            if cur_sum < 0:
                cur_sum = 0
                pointer = i + 1

    print("msf: ", max_so_far)
    print("start_index: ", start_index)
    print("end_index: ", end_index)
    return arr[start_index:end_index + 1]  # splicing, with incursion of the end element itself.


arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
print("max sum of contiguous sum: ", large_contiguous_sum(arr))
