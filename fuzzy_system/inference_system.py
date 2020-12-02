from .fuzzy_set import fuzzy_set

class Evaluable:

    def __init__(self, function = None):
        self.function = function

    def evaluate(self, x):
        return self.function(x)

class Atom:
    def __init__(self, variable, domain):
        self.function = variable[domain].function

    def evaluate(self, x):
        return self.function(x)

    def __or__(self, other):
        return Evaluable(lambda x: max(self.evaluate(x), other.evaluate(x)))

    def __and__(self, other):
        return Evaluable(lambda x: min(self.evaluate(x), other.evaluate(x)))

class Rule:

    def __init__(self, antecedents, consecuent, conjunction = True, larsen = True):
        self.antecedents = antecedents
        self.consecuent = consecuent
        self.conjunction = conjunction
        self.larsen = larsen

    def evaluate(self, pairs):
        values = []

        for p in pairs:
            if p[0] in self.antecedents.keys():
                values.append(self.antecedents[p[0]][p[1]])
        
        value = max(values) if self.conjunction else min(values)

        antecedent_fuzzy = fuzzy_set(self.consecuent.domain, lambda x: value)

        return antecedent_fuzzy.inter_product(self.consecuent) if self.larsen else antecedent_fuzzy.min(self.consecuent)

class Inferencer:

    def __init__(self, variables, defuzzy, larsen = True):
        self.variables = variables
        self.larsen = larsen
        self.rules = []
        self.defuzzy = defuzzy

    def addRule(self, antecedents, consecuent, conjunction = True):
        rule_antecedents = {}

        for ant in antecedents:
            variable, domain = ant.split(' is ')
            rule_antecedents[variable.strip()] = self.variables[variable.strip()][domain.strip()]

        variable, domain = consecuent.split(' is ')
        rule_consecuent = self.variables[variable.strip()][domain.strip()]

        self.rules.append(Rule(rule_antecedents, rule_consecuent, conjunction, self.larsen))

    def evaluate(self, pairs):
        sets = []

        for rule in self.rules:
            sets.append(rule.evaluate(pairs))

        acc_set = sets[0]

        for i in range(1,len(sets)):
            acc_set = acc_set.max(sets[i])

        return self.defuzzy(acc_set)