def return_evens(sequence):
    """
    Using a list comprehension, return a list of all even elements 
    from a sequence of integers.
    
    Args:
        sequence: A sequence of integers
        
    Returns:
        A list containing only the even numbers from the input sequence
    """
    return [n for n in sequence if n % 2 == 0]


def make_exclamation(sentences):
    """
    Using a list comprehension, take a list of sentence strings and 
    return a list of sentence strings with exclamation marks at the end.
    
    Args:
        sentences: A list of sentence strings
        
    Returns:
        A list of the same sentences with exclamation marks added
    """
    return [sentence + "!" for sentence in sentences]