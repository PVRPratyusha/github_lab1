"""
Simple calculator module with basic arithmetic operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent

def sqrt(n):
    """Calculate square root of n."""
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return n ** 0.5

def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot perform modulo with zero!")
    return a % b

def absolute(n):
    """Return absolute value of n."""
    return abs(n)