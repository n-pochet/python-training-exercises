def to_file(filename, obj):
    if obj is None:
        obj = ""
    with open(filename, 'w') as f:
        f.write(str(obj))