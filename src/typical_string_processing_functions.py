def is_palindrome(string: str) -> bool:
    """
    Is the string a palindrome?
    :param string:
    :return:
    """
    length = len(string)
    for i in range(int(length / 2)):
        if string[i] != string[-i - 1]:
            return False
    return True


assert is_palindrome("HelloolleH") is True
assert is_palindrome("Hello") is False
assert is_palindrome("") is True


def extract_filename_and_extension(string: str) -> tuple:
    """
    Extracts filename and extension of given string.
    :param string:
    :return:
    """
    dot = string.index(".")
    base = string[0:dot]
    extension = string[dot+1:]
    return base, extension

assert ("test", "txt") == extract_filename_and_extension("test.txt")


def is_list_of_strings_sorted(list : list) -> bool:
    for i in range(1,len(list)):
        if list[i-1] > list[i]:
            return False
    return True

assert is_list_of_strings_sorted(["hello", "world"]) is True
assert is_list_of_strings_sorted(["world", "hello"]) is False

