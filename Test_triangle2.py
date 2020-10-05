import pytest
from .triangle import Triangle


def test_normal_triangle():
    triangle=Triangle([15,8],[17,7],[16,6])
    triangle.area()
    assert triangle.s==1.51, 'area is wrong'

def test_zero_value():
    triangle=Triangle([0,0],[17,7],[16,6])
    triangle.area()
    assert triangle.s==5.07, 'area is wrong'

def test_float_numbers():
    triangle=Triangle([15.5,8.6],[17.2,7.3],[16,6])
    triangle.area()
    assert triangle.s==1.89, 'area is wrong'

