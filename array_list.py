# moduld to append python a list or array to a file.

import json

array_elements = input("array list elements (seperated by commas): ")
array_list = array_elements.split(",")

with open("list.json", "w") as file:
        json.dump([int(x) for x in array_list], file)


with open("list.json", "r") as file:
    arr = json.load(file)

print(arr)