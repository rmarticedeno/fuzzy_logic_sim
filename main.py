from wifiuh import distance, people, aps, qual, rule1_antecedents, rule1_consecuents, rule2_antecedents, rule2_consecuents, rule3_antececents, rule3_consecuents
from fuzzy_system import Inferencer, Defuzzy


variables = {}

for i in [distance, people, aps, qual]:
    variables[i.name] = i

larsen = Inferencer(variables, Defuzzy.bisectriz)
mamdani = Inferencer(variables, Defuzzy.bisectriz, False)

larsen.addRule(rule1_antecedents, rule1_consecuents, False)
larsen.addRule(rule2_antecedents, rule2_consecuents, False)
larsen.addRule(rule3_antececents, rule3_consecuents)

mamdani.addRule(rule1_antecedents, rule1_consecuents, False)
mamdani.addRule(rule2_antecedents, rule2_consecuents, False)
mamdani.addRule(rule3_antececents, rule3_consecuents)


distance_val = input("Introduzca el valor de distancia al AP mas cercano [1-50]: ")

while not(1 <= int(distance_val) <= 50) :
    distance_val = input("Introduzca el valor de distancia al AP mas cercano [1-50]: ")

personas_val = input("Introduzca el valor correspondiente al número de personas cercanas al usario [1-40]: ")

while not(1 <= int(personas_val) <= 40):
    personas_val = input("Introduzca el valor correspondiente al número de personas cercanas al usario [1-40]: ")

naps_val = input("Introduzca el número de puntos de acceso cercanos al usuario [1-5]: ")

while not(1 <= int(naps_val) <= 5):
    naps_val = input("Introduzca el número de puntos de acceso cercanos al usuario [1-5]: ")

# distance_val = "20"
# personas_val = "20"
# naps_val = "3"

pairs = [("DistanciaAP", int(distance_val)), ("NPersonas", int(personas_val)), ("NAps", int(naps_val))]

larsen_result = larsen.evaluate(pairs)

mamdani_result = mamdani.evaluate(pairs)

print(f"El resultado de inferir la calidad del servicio de wifiuh mediante larsen es {larsen_result}")
print(f"El resultado de inferir la calidad del servicio de wifiuh mediante mamdani es {mamdani_result}")
