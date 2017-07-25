"""
Testing for the math.py module.
"""

import friendly_computing_machine as fcm
import pytest

def test_add():
    assert fcm.math.add(5,2)  == 7
    assert fcm.math.add(2,5) == 7
    assert fcm.math.add(1,2) == 3
#
#def test_mult():
#   assert fcm.math.mult(5,2) == 10
#   assert fcm.math.mult(-5,2) == -10
#
#def test_is_greater_than():
#    assert fcm.math.is_greater_than(4,1) == True
#    assert fcm.math.is_greater_than(1,4) == False
#    assert fcm.math.is_greater_than(4,-1) == True
#    assert fcm.math.is_greater_than(4,4) == False
#

testdata  = [
    (2, 5, 10),
    (1, 2, 2),
    (11, 9, 99),
    (11, 0, 0),
    (0, 0, 0),
]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_mult(a, b, expected):
    assert fcm.math.mult(a, b) == expected
    assert fcm.math.mult(b, a) == expected
