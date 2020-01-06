import re


def replace_dots(s):
    return re.sub(r"\.", "-", s)


def test_replace_dots():
    assert replace_dots("") == ""
    assert replace_dots("no dots") == "no dots"
    assert replace_dots("one.two.three") == "one-two-three"
    assert replace_dots("........") == "--------"
