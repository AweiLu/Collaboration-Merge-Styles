# calculator.py this is c2
def add(a, b):
    """將兩個數字相加"""
    return a + b


def subtract(a, b):
    """將兩個數字相減"""
    return a - b


def multiply(a, b):
    """將兩個數字相乘"""
    return a * b


def divide(a, b):
    """將兩個數字相除"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
