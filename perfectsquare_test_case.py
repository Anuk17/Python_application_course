from perfectsquare import *

def test_square_root_using_math_module():
    n = 16
    obj = FindSquareRoot(n)
    result = obj.square_root()
    print(result)
    assert result*result == n

def test_square_root_pes():
    n = 14
    obj = FindSquareRoot(n)
    result = obj.square_root()
    print(result)
    assert result*result == n

def test_square():
    n = 14
    obj = FindSquareRoot(n)
    result = obj.square_root()
    print(result)
    assert result*result == n
