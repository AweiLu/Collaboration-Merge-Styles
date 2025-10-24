# calculator.py - feature 1: Basic Arithmetic Operations
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

def power(a, b):
    """將a提升到b次方"""
    return a ** b