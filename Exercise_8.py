def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

def uses_all(word, required):
    """Checks whether a word uses all required letters using uses_any.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    for letter in required:
        # Check if the word contains this specific required letter
        if not uses_any(word, letter):
            return False

    return True
#Google AI assistant 10/23/2026, got essentially the same result as the book