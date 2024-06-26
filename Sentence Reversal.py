# simple code block to reverse an inputted string or combination of strings.

def reverse(sentence):
    white_space = " "
    sentence_segmented = sentence.split(white_space)  # seperate the sentence into segments via white spaces.

    rev = sentence_segmented[::-1]  # returns segments starting from the last index.
    rev_sentence = " ".join(rev)  # segments are attached via white-space.
    rev_sentence = rev_sentence.strip(white_space)  # remove trailing and preceeding white spaces.
    return rev_sentence

sentence = str(input("sentence to be reversed: "))
print(sentence)
print(reverse(sentence))
