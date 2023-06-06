def filter_list(l):
    'return a new list with the strings filtered out'
    sp = []
    for i in l:
        if type(i) != str:
            sp.append(i)
        return sp
            