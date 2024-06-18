#  array pair sum.

#  given an integer array,
#  output all unique pairs that sum up to "k".

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

arr_elements = input("Enter elements separated by commas: ")
arr_list = arr_elements.split(',')
arr = []
for x in arr_list:
    arr.append(int(x))

print(arr)
k = int(input("input integer to locate its pair sum: "))
print(pair_sum(arr, k))



