from app.employee import add, multiply


def test_add():
    assert add(1, 2) == 3
    assert add(0, 10) == 10


def test_multiply():
    assert multiply(10, 20) == 200


def test_a():
    assert 9+5 == 14
    assert 10*2 == 20
    assert 5-4 == 1
    assert 200*0 == 0
