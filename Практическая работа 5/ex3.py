def incr(x):
    if x != 10:
        x += 1
    return x


def test_incr():
    assert incr(0) == 1
    assert incr(10) == 10
