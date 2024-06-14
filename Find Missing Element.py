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
    if len(a1) == len(a2):
        return "No missing element."
    else:
        seen = set()
        while a1 < a2:
            for k in a1 not in a2:
                return k
        seen.add(k)


arr = [1, 2, 3, 4, 5]
print(make_array(arr))
print(contrast_between_arrays(arr, make_array(arr)))
