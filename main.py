from wifiuh import distance, people, aps, qual, rule1_antecedents, rule1_consecuents, rule2_antecedents, rule2_consecuents, rule3_antececents, rule3_consecuents
from fuzzy_system import Inferencer, Defuzzy

variables = [distance, people, aps, qual]

larsen = Inferencer(variables, Defuzzy.centroid)
mamdani = Inferencer(variables, Defuzzy.centroid, False)

distance_val = input("Introduzca el valor de distancia al AP mas cercano [1-50]")

while not(1 <= distance_val <= 50) :
    distance_val = input("Introduzca el valor de distancia al AP mas cercano [1-50]")

personas_val = input("Introduzca el valor correspondiente al número de personas cercanas al usario [1-40]")

while not(1 <= personas_val <= 40):
    personas_val = input("Introduzca el valor correspondiente al número de personas cercanas al usario [1-40]")

naps_val = input("Introduzca el número de puntos de acceso cercanos al usuario [1-5]")

while not(1 <= naps_val <= 5):
    naps_val = input("Introduzca el número de puntos de acceso cercanos al usuario [1-5]")

pairs = [("DistanciaAP", distance_val), ("NPersonas", personas_val), ("NAps", naps_val)]

larsen_result = larsen.evaluate(pairs)

mamdani_result = mamdani.evaluate(pairs)

print(f"El resultado de inferir mediante larsen es {larsen_result}")
print(f"El resultado de inferir mediante mamdani es {mamdani_result}")
