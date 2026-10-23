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

def uses_all(word, required):
    """Checks whether a word uses all available letters.

    >>> uses_all('banana', 'ape')
    False
    >>> uses_all('apple', 'apl')
    True
    >>> uses_all('elementary', 'ayls')
    False
    """
    return uses_only(required, word)