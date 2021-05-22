#value = add(2, 2)
#print(value)

#esto de po si va  a dar error por que en la esta hoja de 
#trabajo no esta definida la función (add)
# para llamar la función add se hace lo siguiente :

#import adder

#hay dos formas de llamar las funciones de otra hoja
#una es con from y otra con import
#estos se diferencian por que al usar solo import es necesario anteponer el nombre de importación con un (.)
#y despues poner el nombre de la funcion. ejplo :

#value = adder.add(2, 2)
#print(value)

#ahora con from :

#import adder

#value = adder.add(2, 2)
#double_value = adder.double(value)
#print(double_value)

#from adder import *

#value = add(2, 2)
#double_value = double(value)
#print(double_value)

#renombrand módulos

#import adder as a 

#value = adder.add(2, 2)
#double_value = adder.double(value)
#print(double_value)

#corrigiendo

#import adder as a 

#value = a.add(2, 2)
#double_value = a.double(value)
#print(double_value)

#from adder import add, double

#value = add(2, 2)
#double_value = double(value)
#mul_value = mul(double_value) 
#print(mul_value)

from adder import add, double

value = add(2, 2)
double_value = double(value)
print(double_value)