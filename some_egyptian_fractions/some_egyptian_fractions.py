"""
Given a rational number n

n >= 0, with denominator strictly positive

    as a string (example: "2/3" in Ruby, Python, Clojure, JS, CS, Go) or as two
    strings (example: "2" "3" in Haskell, Java, CSharp, C++, Swift)

    or as a rational or decimal number (example: 3/4, 0.67 in R)

decompose this number as a sum of rationals with numerators equal to one and
without repetitions (2/3 = 1/2 + 1/6 is correct but not 2/3 = 1/3 + 1/3, 1/3 is
repeated).

The algorithm must be "greedy", so at each stage the new rational obtained in
the decomposition must have a denominator as small as possible. In this manner
the sum of a few fractions in the decomposition gives a rather good
approximation of the rational to decompose.

2/3 = 1/3 + 1/3 doesn't fit because of the repetition but also because the first
1/3 has a denominator bigger than the one in 1/2 in the decomposition
2/3 = 1/2 + 1/6.
Example:

(You can see other examples in "Sample Tests:")
"""

import math


def _decompose(x, y):
    if x == 0:
        return []
    f1 = math.ceil(y / x)
    return [f1] + _decompose((-y) % x, y * math.ceil((y / x)))


def decompose(n):
    try:
        x, y = (int(z) for z in n.split('/'))
    except ValueError:
        y = 1
        x = float(n)
        while math.floor(x) != math.ceil(x):
            x = x * 10
            y = y * 10
        x = int(x)
    if x != 0 and math.ceil(x / y) == math.floor(x / y):
        return [str(int(x / y))]
    denominators = _decompose(x, y)
    return ['1/{}'.format(d) if d != 1 else '1' for d in denominators]


def test_sample():
    assert decompose('0') == []
    assert decompose('3/4') == ["1/2", "1/4"]
    assert decompose('4/5') == ["1/2", "1/4", "1/20"]
    assert decompose('0.66') == ["1/2", "1/7", "1/59", "1/5163", "1/53307975"]
    assert decompose('75/3') == ["25"]

    assert decompose("21/23") == ["1/2", "1/3", "1/13", "1/359", "1/644046"]

    assert decompose('2/3') == ['1/2', '1/6']

    decompose('5/4')