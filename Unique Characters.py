# Check if a string of characters is unique.
def unique_char(string):
    pointer = 0
    seen = set()
    while pointer < len(string):
        if string[pointer] in seen:  # all indices are already stored in seen.
            return "False, this string is not of unique characters."
        seen.add(string[pointer])
        pointer += 1
    return seen, "True, this string is of unique characters."

string = input("string: ")
print(unique_char(string))
