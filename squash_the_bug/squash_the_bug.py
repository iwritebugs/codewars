"""
Simple challenge - eliminate all bugs from the supplied code so that the code
runs and outputs the expected value. Output should be the length of the longest
word, as a number.

There will only be one 'longest' word.
"""


def find_longest(string):
    return max(len(x) for x in string.split(' '))
    # spl = string.split(" ")
    # longest = 0
    # i = 0
    # while (i < len(spl)):
    #     if (len(spl[i]) > longest):
    #         longest = len(spl[i])
    #     i += 1
    # return longest


def test_find_longest():
    assert find_longest(
        "The quick white fox jumped around the massive dog") == 7
    assert find_longest("Take me to tinseltown with you") == 10
    assert find_longest("Sausage chops") == 7
    assert find_longest("Wind your body and wiggle your belly") == 6
    assert find_longest("Lets all go on holiday") == 7
