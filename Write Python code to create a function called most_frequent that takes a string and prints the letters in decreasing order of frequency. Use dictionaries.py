W= input('Please enter a string ')
def most_frequent(string):
    import operator
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

print (most_frequent(W))
