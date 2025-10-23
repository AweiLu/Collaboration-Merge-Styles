# test_calculator.py
import pytest
import sys
import os

# 將 .github 目錄添加到 Python 路徑
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(3, 3) == 9


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)
