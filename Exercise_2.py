def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('encyclopedia', 'qtv')
    True
    """
    for letter in forbidden:
        if letter in word.lower():
            return False
    return True

print(uses_none('banana', 'xyz'))
print(uses_none('apple', 'efg'))
print(uses_none('encyclopedia', 'qtv'))
