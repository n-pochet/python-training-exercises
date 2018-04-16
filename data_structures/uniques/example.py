def uniques(elts):
    """Unique elements, sorted
    
    Arguments:
        elts {list} -- List of elements
    
    Returns:
        list -- List of sorted unique elements
    """

    if elts is None:
        return []
    unique_elts = list(set(elts))
    unique_elts.sort()
    return unique_elts