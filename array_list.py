# module to append multiple python lists to a file.

import sys
import os
import json

def my_array_lists(filename, list_name, arr):
# attempting to read from file.
        if os.path.exists(filename) and os.path.getsize(filename) > 0: # if the file exists and if it is not empty.
                try:
                        with open(filename, "r") as file:
                                data = json.load(file)
                except FileNotFoundError or json.JSONDecodeError: # while the file doesn't exist & if the file content
                        # is not valid JSON...
                        data = {} # ...initialize our dictionary.
        else: # no error code...
                data = {} # ...initialize dictionary.

        data[list_name] = arr

        with open(filename, "w") as file: # write our updated dictionary to the file.
            json.dump(data, file, indent=4)


array_elements = input("array list elements (seperated by commas): ")
try:
        array_list = [int(x) for x in array_elements.split(",")]
        arr = array_list
except ValueError:
        print("Enter whole numbers as array elements.")
        sys.exit()
filename = "list.json"
list_name = input("name the array list: ")

my_array_lists(filename, list_name, arr)
# print(f"{list_name} : {arr}")