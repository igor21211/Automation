import pytest

@pytest.fixture()
def first_fixture():
    print(f'First job')



def test_01 (first_fixture):
    s = [1, 3, 4, 'Tom', 4, 2, 5, 'David', 'Jan']
    return s.index('Tom') in s


def test_02 (first_fixture):
    e = 'Adam'
    return e == e.lower()[::-1]

def test_03(first_fixture):
    d = [i for i in range(10)]
    return len(d) == d[9]

def test_04(first_fixture):
    q = ['Adam', ' David', 'Marcus']
    assert 3 == len(q)

