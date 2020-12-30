import math

#valor =(peso/maxpeso)*1

pesos = [4.3, 400.65,44.6,453.45,3.4,1245.6,5000.4]

maior = max(pesos)
menor = min(pesos)

d1=0
d2=1.0

for a in pesos:
    print(((a-menor)*(d2-d1)/(maior-menor))+d1)
