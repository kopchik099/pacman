def open_or_senior(data):
    res = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            res.append('Senior')
        else:
            res.append('Open')
    return res