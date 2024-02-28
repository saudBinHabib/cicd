# Function to be tested
def add(a, b):
    return a + b


# Test case for positive numbers
def test_positive_numbers():
    assert add(1, 2) == 3  # Expected result: 1 + 2 = 3


# Test case for negative numbers
def test_negative_numbers():
    assert add(-1, -2) == -3  # Expected result: -1 + (-2) = -3


# Test case for one positive and one negative number
def test_mixed_numbers():
    assert add(1, -2) == -1  # Expected result: 1 + (-2) = -1


# Test case for zero
def test_zero():
    assert add(0, 0) == 0  # Expected result: 0 + 0 = 0
