# programa para simular el lanzamiento de un dado

import random

print ("------------------------------")
print ("----LANZAMIENTO DE UN DADO----")
print ("------------------------------")

#input 

#processing
d = random.randint(1,6)

if (d==1):
    rta = "UNO"
elif (d==2):
    rta = "DOS"
elif (d==3):
    rta = "tres"
elif (d==4):
    rta = "CUATRO"
elif (d==5):
    rta = "CINCO"
elif (d==6):
    rta = "SEIS"
else:
    rta = "no es la cara de un dado"

#ouput 
print "el dado cayo en "+ str (rta)

