def find_longest_word(document, longest_word=""):
    if document is None:
        return longest_word

    new_list = document.split(" ", maxsplit=1)
    # print("NEW_LIST = ",new_list," LONGEST_WORD:",longest_word)
    if len(new_list) == 1:
        longest_word = new_list[0] if len(new_list[0]) > len(longest_word) else longest_word
        return longest_word

    if len(new_list[0]) > len(longest_word):
        # print("NEW LONGEST WORD:", new_list[0])
        return find_longest_word(new_list[1],new_list[0])
    else:
        # print("NOT LONGEST WORD:", new_list[0])
        return find_longest_word(new_list[1],longest_word)
