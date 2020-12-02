from fuzzy_system import LinguisticVariable, MembershipFunction

near_dist_func = lambda x: MembershipFunction.L(x, 10, 15)
mid_dist_func = lambda x: MembershipFunction.Pi(x, 10, 15, 30, 35)
far_dist_func = lambda x: MembershipFunction.Gamma(x, 30, 35)

distance_functions = [near_dist_func, mid_dist_func, far_dist_func]

distance_domain = [i for i in range(51)]

distance_terms = ['Cercana', 'Media', 'Lejana']

# Distancia al Ap mas cercano
distance = LinguisticVariable("DistanciaAP", distance_domain, distance_terms, distance_functions)

#############################################################################################

few_people_func = lambda x: MembershipFunction.Z(x, 0, 15)
some_people_func = lambda x: MembershipFunction.Gaussian(x, 20, 10)
many_people_func = lambda x: MembershipFunction.S(x, 25, 40)

people_functions = [few_people_func, some_people_func, many_people_func]

people_domain = [i for i in range(41)]

people_terms = ['Pocas', 'Algunas', 'Muchas']

# Numero de personas cercanas
people = LinguisticVariable("NPersonas", people_domain, people_terms, people_functions)

#############################################################################################

few_aps_func = lambda x: MembershipFunction.Lambda(x, -2, 2, 0)
some_aps_func = lambda x: MembershipFunction.Pi(x, 1, 2, 3, 4)
many_aps_func = lambda x: MembershipFunction.Lambda(x, 3, 5, 4)

aps_functions = [few_aps_func, some_aps_func, many_aps_func]

aps_domain = [i for i in range(6)]

aps_terms = ['Pocos', 'Algunos', 'Varios']

# Numero de antenas cercanas
aps = LinguisticVariable("NAps", aps_domain, aps_terms, aps_functions)

#############################################################################################

poor_qual_func = lambda x: MembershipFunction.L(x, 0, 4)
middle_qual_func = lambda x: MembershipFunction.Pi(x, 2, 4, 6, 8)
exc_qual_func = lambda x: MembershipFunction.Gamma(x, 6, 8)

qual_functions = [poor_qual_func, middle_qual_func, exc_qual_func]

qual_domain = [i for i in range(11)]

qual_terms = ['Pobre', 'Regular', 'Buena']

# Calidad de la señal
qual = LinguisticVariable("Calidad", qual_domain, qual_terms, qual_functions)