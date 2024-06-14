# finding the missing element from a randomized array.

# given an array of non-negative integers. A second array is formed by shuffling
# the elements in the first array and then deleting a random element. given the two arrays,
# find which elements is missing.

import numpy as np


def make_array(arr):

    b_arr = np.array(arr)  # initialize array to numpy array.
    np.random.shuffle(b_arr)  # shuffle the array

    # delete a random element and return the "new" array.
    random_index = np.random.randint(0, len(b_arr))  # choosing a random integer from the array.
    b_arr = np.delete(b_arr, random_index)  # delete the random integer and attach the new array to variable "b_arr"
    return b_arr


def contrast_between_arrays(arr_1, arr_2):
    # sorting both arrays.
    a1 = sorted(arr_1)
    a2 = sorted(arr_2)
    seen = {}  # create a dictionary for storing seen elements in both array.
    for element in a1:
        if element in seen:
            seen[element] += 1

        else:
            # if element not in seen, append to "seen".
            seen[element] = 1

    for element in a2:
        # if element in seen, "displace" from "seen".
        if element in seen:
            seen[element] -= 1
        else:
            seen[element] = 1

    for k in seen:
        # if the difference in elements between the first and second arrays does not equal 0, return k.
        # "k" being the outlier element.
        if seen[k] != 0:
            return k
    return "No missing elements"


arr = [1, 2, 3, 4, 5]
original_array = np.array(arr)
shuffled_and_deleted_array = make_array(arr)
print(original_array)
print(shuffled_and_deleted_array)
print(contrast_between_arrays(original_array, shuffled_and_deleted_array))

