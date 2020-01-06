


def round_by_2_decimal_places(n):
    from decimal import Decimal, ROUND_HALF_UP
    return Decimal(n.quantize(exp=Decimal('0.01'), rounding=ROUND_HALF_UP))



def test_round_by_2_decimal_places():
    from decimal import Decimal

    assert round_by_2_decimal_places(Decimal('2')) == Decimal('2')
    assert round_by_2_decimal_places(Decimal('7.477')) == Decimal('7.48')
    assert round_by_2_decimal_places(Decimal('-4.999')) == Decimal('-5')
    assert round_by_2_decimal_places(Decimal('18.123')) == Decimal('18.12')
    assert round_by_2_decimal_places(Decimal('0')) == Decimal('0')
    assert round_by_2_decimal_places(Decimal('1.455')) == Decimal('1.46')
    assert round_by_2_decimal_places(Decimal('-1.455')) == Decimal('-1.46')
    assert round_by_2_decimal_places(Decimal('1.055')) == Decimal('1.06')
    assert round_by_2_decimal_places(Decimal('-1.055')) == Decimal('-1.06')
    assert round_by_2_decimal_places(Decimal('16.765')) == Decimal('16.77')
    assert round_by_2_decimal_places(Decimal('-16.765')) == Decimal('-16.77')
    assert round_by_2_decimal_places(Decimal('1.025')) == Decimal('1.03')
    assert round_by_2_decimal_places(Decimal('-1.025')) == Decimal('-1.03')
    assert round_by_2_decimal_places(Decimal('16.355')) == Decimal('16.36')
    assert round_by_2_decimal_places(Decimal('-16.345')) == Decimal('-16.35')
    assert round_by_2_decimal_places(Decimal('-1.1949999999999999999999999999')) == Decimal('-1.19')
    assert round_by_2_decimal_places(Decimal('-1.1950000000000000000000000001')) == Decimal('-1.2')
    assert round_by_2_decimal_places(Decimal('1.1949999999999999999999999999')) == Decimal('1.19')
    assert round_by_2_decimal_places(Decimal('1.1950000000000000000000000001')) == Decimal('1.2')
    assert round_by_2_decimal_places(Decimal('-1.1849999999999999999999999999')) == Decimal('-1.18')
    assert round_by_2_decimal_places(Decimal('-1.1850000000000000000000000001')) == Decimal('-1.19')
    assert round_by_2_decimal_places(Decimal('1.1849999999999999999999999999')) == Decimal('1.18')
    assert round_by_2_decimal_places(Decimal('1.1850000000000000000000000001')) == Decimal('1.19')