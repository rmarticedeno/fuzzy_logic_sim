

class Defuzzy:

    @staticmethod
    def centroid(fuzzy):
        a = sum([x * fuzzy.function(x) for x in fuzzy.domain])
        b = sum([fuzzy.function(x) for x in fuzzy.domain])
        return a/b

    #Todo
    @staticmethod
    def bisectriz(fuzzy):
        area = 0
        image = [fuzzy.function(x) for x in fuzzy.domain]
        pairs = zip(fuzzy.domain, image)

        for x,y in pairs:
            area += x*y
        
        area_acc = 0
        index = 0

        while(area/2 >= area_acc):
            area_acc += fuzzy.domain[index] * image[index]
            index += 1
        
        return fuzzy.domain[index-1]
    
    @staticmethod
    def central_max(fuzzy):
        values = _find_maxs(fuzzy)
        return values[int(len(values)/2)]

    @staticmethod
    def smallest_max(fuzzy):
        return min(_find_maxs(fuzzy))

    @staticmethod
    def bigger_max(fuzzy):
        return max(_find_maxs(fuzzy))



def _find_maxs(fuzzy):
    _max = 0
    for i in fuzzy.domain:
        if fuzzy.function(i) > _max:
            _max = fuzzy.function(i)

    return [ i for i in fuzzy.domain if fuzzy.function(i) == _max]