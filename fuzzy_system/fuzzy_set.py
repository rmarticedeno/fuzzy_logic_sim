class fuzzy_set:

    def __init__(self, Values, pertenence_function, id = None):
        self.domain = Values
        self.function = pertenence_function
        self.id = id

    def altura(self):
        max = 0
        for i in self.domain:
            value = self.function(i)
            if value > max:
                max = value
        return max

    def soporte(self):
        result = []
        for i in self.domain:
            if self.function(i) > 0:
                result.append(i)

        return result

    def nucleo(self):
        result = []
        for i in self.domain:
            if self.function(i) == 1:
                result.append(i)
        return result

    def normalización(self):
        return [self.function[i]/self.altura for i in self.domain]

    def puntos_de_cruce(self):
        return [i for i in self.domain if self.function(i) == 0.5]

    def alfa_corte(self, alfa):
        return [i for i in self.domain if self.function(i) > alfa]

    def frontera(self):
        return [i for i in self.domain if 0 < self.function(i) < 1 ]

    def __eq__(self, other):
        for x in self.domain:
            if self.function[x] != other.function[x]:
                return False
        return True

    def __getitem__(self, x):
        return self.function(x)

    def complement(self):
        return fuzzy_set(self.domain, lambda x : 1 - self.function(x))
    
    # Union T Conorms
    def max(self, other):
        return _generate_fuzzy(self, other, lambda x,y,z : max(x.function(z),y.function(z)))

    def union_product(self, other):
        return _generate_fuzzy(self, other, lambda x,y,z : (x.function(z) + y.function(z)) - x.function(z) * y.function(z))

    def Lukasiewick_sum(self, other):
        return _generate_fuzzy(self, other, lambda x,y,z: min(x.function(z) + y.function(z), 1))

    # Intersection T Conorms
    def min(self, other):
        return _generate_fuzzy(self, other, lambda x,y,z : min(x.function(z),y.function(z)))
    
    def inter_product(self, other):
        return _generate_fuzzy(self, other, lambda x,y,z : (x.function(z) * y.function(z)))

    def Lukasiewick_diff(self, other):
        return _generate_fuzzy(self, other, lambda x,y,z: min(0, x.function(z) + y.function(z) - 1))


def _generate_fuzzy(set1, set2, function):
    values = {} 
    for x in set1.domain:
        values[x] = function(set1, set2, x)
    return fuzzy_set(set1.domain, lambda x : values[x])