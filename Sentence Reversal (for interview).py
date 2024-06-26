# an interview problem to reverse the order of words in a given sentence.

import json
import array_list

def reverse(sentence):
    words = []
    white_spaces = " "
    length_sen = len(sentence)
    pointer = 0

    while pointer < length_sen:
        if sentence[pointer] not in white_spaces:  # if the pointer is not on a white space,
            # it must be on a letter.
            start_index = pointer  # first letter is now start index and start index is where the
            # the pointer is located.
            while pointer < length_sen and sentence[pointer] not in white_spaces:  # nested while loops for multiple
                # iterations till the end.
                pointer += 1
            words.append(sentence[start_index:pointer])
        pointer += 1

    return " ".join(reversed(words))


