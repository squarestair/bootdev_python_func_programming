from functools import lru_cache


@lru_cache
def is_palindrome(word):
    if len(word) < 2:
        return True
    if len(word) == 2:
        return word[0] == word[1]
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
