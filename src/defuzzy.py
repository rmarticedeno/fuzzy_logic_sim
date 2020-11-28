
def centroid(fuzzy):
    a = sum([x * fuzzy.function(x) for x in fuzzy.domain])
    b = sum([fuzzy.function(x) for x in fuzzy.domain])
    return a/b

#Todo
def bisectriz(fuzzy):
    pass

def central_max(fuzzy):
    values = _find_maxs(fuzzy)
    return values[int(len(values)/2)]

def smallest_max(fuzzy):
    return min(_find_maxs(fuzzy))

def bigger_max(fuzzy):
    return max(_find_maxs(fuzzy))

def _find_maxs(fuzzy):
    _max = 0
    for i in fuzzy.domain:
        if fuzzy.function(i) > _max:
            _max = fuzzy.function(i)

    return [ i for i in fuzzy.domain if fuzzy.function(i) == _max]