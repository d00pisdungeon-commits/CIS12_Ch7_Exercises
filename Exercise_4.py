def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('apple', 'apl')
    True
    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True