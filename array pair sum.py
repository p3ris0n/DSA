#  array pair sum.

#  given an integer array,
#  output all unique pairs that sum up to "k".

import json
import sys

def pair_sum(arr, k):
    arr.sort()
    pointer_1 = 0  # initializing pointer_1 at the start of the array.
    pointer_2 = len(arr) - 1  # initializing pointer_2 at the end of the array.
    pairs = []  # a list to keep track of the pairs.
    seen = set()  # a set to keep track of uniqueness (of the pairs)

    while pointer_1 < pointer_2:
        current_sum = arr[pointer_1] + arr[pointer_2]
        pair = arr[pointer_1], arr[pointer_2]
        if current_sum == k:
            pairs.append(pair)
            seen.add(pair)
            pointer_2 -= 1

        if current_sum < k:
            pointer_1 += 1
        if current_sum > k:
            pointer_2 -= 1

    return pairs if pairs else "No pair sum."


print("---Find array sum pairs---")
print(f"---Get list from 'list.json' file---")

# reading array data from file

with open("list.json", "r") as file:
    data = json.load(file)
listname = str(input("array list's name: "))
if listname not in data:
    print("no such list in file.")
    sys.exit()
else:
    arr = data.get(listname, [])
    k = int(input("value to locate its pair sum(s): "))
    print(pair_sum(arr, k))
    print("array used: ", arr)