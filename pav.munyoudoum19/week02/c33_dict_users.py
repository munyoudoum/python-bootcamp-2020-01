def dict_users(ls):
    return [{'username': ls[i], 'ID': i+1} for i in range(len(ls))]
