def correct_tail(body, tail):
    return body.endswith(tail)


def test_correct_tail():
    assert correct_tail("Fox", "x") == True
    assert correct_tail("Rhino", "o") == True
    assert correct_tail("Meerkat", "t") == True
    assert correct_tail("Emu", "t") == False
    assert correct_tail("Badger", "s") == False
    assert correct_tail("Giraffe", "d") == False
