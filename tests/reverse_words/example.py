def reverse(words):
    """Reverse a string containing several words
    
    Arguments:
        words {str} -- The words to reverse
    
    Returns:
        str -- The reversed words
    """

    if words is None:
        return ""
    else:
        words = list(filter(lambda w: w != "", words.split(" ")))
        words.reverse()
        return " ".join(words)
