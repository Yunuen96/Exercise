# autor:Cassandra Alcázar Dávila
# programa:Actividad 9
# realización:Viernes 7 de noviembre del 2014.
#Construya un programa en Scratch tal que dado como dato el sueldo de un trabajador, le aplique un aumento del 15% si su sueldo es inferior a $1,000.00 y 12% en caso contrario. Imprima el nuevo sueldo del trabajador.
######## ########  ######## ########
sueldo = input ("inserta sueldo")
if sueldo <1000 or sueldo == 1000:
    sueldo = (sueldo * .15 )
else:
    sueldo = (sueldo * .12)
print sueldo

