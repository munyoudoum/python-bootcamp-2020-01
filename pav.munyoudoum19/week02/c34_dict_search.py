def dict_search(info_students, key):
    return info_students.get(key, "ERROR: '{}' key not found.".format(key))
