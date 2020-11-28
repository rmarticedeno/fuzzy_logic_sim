from fuzzy_set import fuzzy_set

class linguistic_variable:

    def __init__(self, name, domain, terms, functions):
        self.name = name
        self.domain = domain
        self.terms = terms
        self.functions = functions
        self.fuzzy_variables = {}
        for i in len(terms):
            self.fuzzy_variables[self.terms[i]] = fuzzy_set(self.domain, functions[i], self.terms[i])
            