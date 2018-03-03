def find_duplicates_in_list_sorted(list_numbers: list) -> list:
    """
    Algorithm to find duplicates in a list of numbers:

    Runtime complexity: O(n log(n))

    :param list_numbers: a list of numbers
    :return: duplicates in a list
    """
    result = []
    # Sort the list
    list_numbers.sort()
    # Iterate over the list
    for i in range(1, len(list_numbers)):
        # If previous element is the same as current, its the duplicated element
        if list_numbers[i] == list_numbers[i - 1]:
            result.append(list_numbers[i])
    return result


def find_missing_numbers(input_list: list) -> list:
    """
    Finds all missing integer numbers.
    
    :param input_list:
    :return: 
    """
    missing_numbers = []
    input_list.sort()
    for i in range(0, len(input_list) - 1):
        if input_list[i + 1] != input_list[i] + 1:
            missing_numbers.append(input_list[i] + 1)
    return missing_numbers


def is_palindrome(input_string):
    """

    Runtime complexity: O(n)
    Space complexity: O(n)

    :param input_string:
    :return:
    """
    for i in range(int(len(input_string) / 2)):
        if input_string[i] != input_string[-i - 1]:
            return False
    return True


def reverse_string(a_string):
    """

    Runtime complexity: O(n)

    :param a_string:
    :return:
    """
    return a_string[::-1]


def fibonacci_recursive(n):
    """
    Recursive Fibonacci algorithm.

    Runtime complexity: O(n)
    Space Complexity: O(n)
    :param n:
    :return:
    """
    if -1 < n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_looping(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fibIterator():
    global a, b
    while True:
        a, b = b, a + b
        yield a


# Fibonacci with memoization
def memoize(fn, arg):
    memo = {}
    if arg not in memo:
        memo[arg] = fn(arg)
        return memo[arg]


# Using memoization as decorator
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]


@Memoize
def decorated_fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fibonacci_with_sequence(n):
    fibo = [0, 1]
    for i in range(n):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo


def flip_vertical_axis_built_in_reversed(matrix):
    """
    You are given an m x n 2D image matrix (List of Lists) where each integer represents a pixel. Flip it in-place along its vertical axis.

    This solution uses the built in "reversed" function.

    :param matrix:
    :return:
    """
    for i in range(len(matrix)):
        matrix[i] = list(reversed(matrix[i]))
    return matrix


def flip_vertical_axis(matrix):
    """

    Runtime complexity: O(n)
    Space complexity: O(1)

    :param matrix:
    :return:
    """
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    temp = 0
    i = 0
    while i <= r:
        j = 0
        while j <= (c / 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][c - j]
            matrix[i][c - j] = temp
            j = j + 1
        i = i + 1


if __name__ == "__main__":
    assert [1, 5] == find_duplicates_in_list_sorted([1, 2, 76, 32, 45, 1, 5, 4, 9, 5])

    assert [3, 9] == find_missing_numbers([1, 2, 10, 8, 6, 7, 5, 4])

    # https://technobeans.com/2012/04/19/5-ways-of-fibonacci-in-python-best-way/
    # https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/
    assert 0 == fibonacci_recursive(0)
    assert 1 == fibonacci_recursive(1)
    assert 55 == fibonacci_recursive(10)

    assert 55 == fibonacci_looping(10)

    a, b = 0, 1
    result = 0
    fib_gen = fibIterator()
    for i in range(10):
        result = next(fib_gen)
    assert 55 == result

    # Fibonacci with memoization
    assert 55 == memoize(fibonacci_looping, 10)

    assert 55 == decorated_fib(10)

    assert [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] == fibonacci_with_sequence(10)

    assert True == is_palindrome("madam") == is_palindrome("aabbaa") == is_palindrome("")
    assert False == is_palindrome("abaa")

    assert "Hello WOrld!" == reverse_string("!dlrOW olleH")

    assert [[0, 1], [0, 1]] == flip_vertical_axis_built_in_reversed([[1, 0], [1, 0]])
    assert [[0, 1], [0, 1]] == flip_vertical_axis([[1, 0], [1, 0]])
