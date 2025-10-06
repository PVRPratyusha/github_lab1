"""
Unit tests for calculator module using pytest.
"""
import pytest
import sys
from pathlib import Path

# Add parent directory to path so we can import src
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.calculator import add, subtract, multiply, divide, power, sqrt, modulo, absolute


class TestCalculator:
    """Test cases for calculator functions."""

    def test_add(self):
        """Test addition function."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction function."""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(10, 10) == 0

    def test_multiply(self):
        """Test multiplication function."""
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0

    def test_divide(self):
        """Test division function."""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError):
            divide(10, 0)

    def test_power(self):
        """Test power function."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 0) == 1
        assert power(2, -1) == 0.5

    def test_sqrt(self):
        """Test square root function."""
        assert sqrt(4) == 2
        assert sqrt(9) == 3
        assert sqrt(0) == 0
        assert sqrt(2) == pytest.approx(1.414, rel=0.01)

    def test_sqrt_negative(self):
        """Test square root of negative raises error."""
        with pytest.raises(ValueError):
            sqrt(-1)

    def test_modulo(self):
        """Test modulo function."""
        assert modulo(10, 3) == 1
        assert modulo(15, 4) == 3
        assert modulo(20, 5) == 0

    def test_modulo_by_zero(self):
        """Test modulo by zero raises error."""
        with pytest.raises(ValueError):
            modulo(10, 0)

    def test_absolute(self):
        """Test absolute value function."""
        assert absolute(-5) == 5
        assert absolute(5) == 5
        assert absolute(0) == 0
        assert absolute(-3.14) == 3.14