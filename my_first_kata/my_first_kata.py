def my_first_kata(a, b):

    def any_bool(*args):
        return any(isinstance(x, bool) for x in args)

    def no_numeric(*args):
        return not all(any(isinstance(x, t) for t in (int, float)) for x in args)

    if any_bool(a,b) or no_numeric(a,b):
        return False

    return (a % b) + (b % a)


def test_my_first_kata():
    assert my_first_kata(3, 5) == (3 % 5 + 5 % 3)
    assert my_first_kata("hello", 3) == False
    assert my_first_kata(67, "bye") == False
    assert my_first_kata(True, True) == False
    assert my_first_kata(314, 107) == (107 % 314 + 314 % 107)
    assert my_first_kata(1, 32) == (1 % 32 + 32 % 1)
    assert my_first_kata(-1, -1) == (-1 % -1 + -1 % -1)
    assert my_first_kata(19483, 9) == (9 % 19483 + 19483 % 9)
    assert my_first_kata("hello", {}) == False
    assert my_first_kata([], "pippi") == False

    assert my_first_kata(False, 5) == False
