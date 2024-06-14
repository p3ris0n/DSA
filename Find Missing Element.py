# finding the missing element from a randomized array.

# given an array of non-negative integers. A second array is formed by shuffling
# the elements in the first array and then deleting a random element. given the two arrays,
# find which elements is missing.

import numpy as np


def make_array(arr):  # taking parameters array and k, k being the deleted element.

    b_arr = np.array(arr)
    np.random.shuffle(b_arr)

    random_index = np.random.randint(0, len(b_arr))
    b_arr = np.delete(b_arr, random_index)
    return b_arr


def contrast_between_arrays(arr_1, arr_2):
    a1 = sorted(arr_1)
    a2 = sorted(arr_2)
    seen = {}
    for element in a1:
        if element in seen:
            seen[element] += 1

        else:
            seen[element] = 1

    for element in a2:
        if element in seen:
            seen[element] -= 1
        else:
            seen[element] = 1

    for k in seen:
        if seen[k] != 0:
            return k
    return "No missing elements"


arr = [1, 2, 3, 4, 5]
original_array = np.array(arr)
shuffled_and_deleted_array = make_array(arr)
print(original_array)
print(shuffled_and_deleted_array)
print(contrast_between_arrays(original_array, shuffled_and_deleted_array))

