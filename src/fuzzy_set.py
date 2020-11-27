class fuzzy_set:

    def __init__(self, Values, pertenence_function):
        self.domain = Values
        self.function = pertenence_function

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
