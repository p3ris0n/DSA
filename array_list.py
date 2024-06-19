# a python file

import json

array_elements = input("array list elements (seperated by commas): ")
array_list = array_elements.split(",")
arr = []
for x in array_list:
    arr.append(int(x))

with open("list.json", "w") as file:
    json.dump(arr, file)

"""with open("list.json", "r") as file:
    arr = json.load(file)"""

