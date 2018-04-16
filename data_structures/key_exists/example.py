def key_exists(dictionary, key):
    """Tests if a key exists in a dictionary
    
    Arguments:
        dictionary {dict} -- The dictionary to test
        key {str} -- The key to test
    
    Returns:
        bool -- `True` if the key exists in the dictionary
    """

    exists = dictionary.get(key, None)
    return exists is not None