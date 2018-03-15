def is_palindrome(characters):
    """Analyses if the characters form a palindrome
    
    Arguments:
        characters {str} -- The characters to analyze
    
    Returns:
        bool -- Returns True if it is a palindrome
    """

    if characters:
        characters = list(filter(lambda c: c != " ", characters))
        return characters == characters[::-1] 
    else:
        return False