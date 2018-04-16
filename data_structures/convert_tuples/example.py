def convert(elts):
    """Convert a list of tuples into a dictionary
    
    Arguments:
        elts {list} -- List of tuples
    
    Returns:
        dict -- List of tuples converted into a dictionary
    """

    if not elts:
        return {}
    
    result = {k: v for (k, v, *_) in elts}
    return result