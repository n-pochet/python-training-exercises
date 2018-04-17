def to_file(filename, obj):
    """To File
    
    Arguments:
        filename {str} -- Path to the file
        obj {object} -- The object to write to the file
    """

    if obj is None:
        obj = ""
    with open(filename, 'w') as f:
        f.write(str(obj))