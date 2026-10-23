def uses_only(word, available):
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('elementary', 'ayl')
    False
    """

    for letter in word.lower():
        if letter not in available.lower():
            return False
    return True