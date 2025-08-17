#!/usr/bin/env python3

from lib.list_comprehension import return_evens, make_exclamation

def test_return_evens():
    """Test the return_evens function"""
    # Test with mixed odd and even numbers
    result = return_evens([0, 1, 3, 5, 7, 8, 9])
    expected = [0, 8]
    print(f"return_evens([0, 1, 3, 5, 7, 8, 9]) = {result}")
    print(f"Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test with all even numbers
    result = return_evens([2, 4, 6, 8])
    expected = [2, 4, 6, 8]
    print(f"return_evens([2, 4, 6, 8]) = {result}")
    assert result == expected
    
    # Test with all odd numbers
    result = return_evens([1, 3, 5, 7])
    expected = []
    print(f"return_evens([1, 3, 5, 7]) = {result}")
    assert result == expected
    
    # Test with empty list
    result = return_evens([])
    expected = []
    print(f"return_evens([]) = {result}")
    assert result == expected
    
    print("✅ All return_evens tests passed!")


def test_make_exclamation():
    """Test the make_exclamation function"""
    # Test with the example from the assignment
    result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
    expected = ["Hello!", "I'm doing great!", "Python is fun!"]
    print(f"make_exclamation([\"Hello\", \"I'm doing great\", \"Python is fun\"]) = {result}")
    print(f"Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test with empty list
    result = make_exclamation([])
    expected = []
    print(f"make_exclamation([]) = {result}")
    assert result == expected
    
    # Test with single sentence
    result = make_exclamation(["Great job"])
    expected = ["Great job!"]
    print(f"make_exclamation([\"Great job\"]) = {result}")
    assert result == expected
    
    print("✅ All make_exclamation tests passed!")


if __name__ == "__main__":
    print("Testing return_evens function:")
    test_return_evens()
    print()
    
    print("Testing make_exclamation function:")
    test_make_exclamation()
    print()
    
    print("🎉 All tests passed! Your list comprehensions are working correctly.")