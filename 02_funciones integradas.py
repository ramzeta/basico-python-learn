# FUNCIONES INTEGRADAS

#Conversiones

n = bin(10)
n = hex(10)
n = int("0b1010",2)
n = int("0xa",16)
print("fundiones = ",n)

#VALOR ABSOLUTO
n=abs(-343)
print("fundiones = ",n)

#Caracteres
n = len("Ramiro")

#Si quieres ver que hace la funcion ponla la ultima
print("fundiones = ",n)


#iter
mi_lista = [1,2+2,3,4,5,6,"HOLA",8,9]


for item in mi_lista:
    print(item)


iterador = iter(mi_lista)
print("iterator",iterador.__next__())
print("iterator",iterador.__next__())

"""
pilou
image to html
"""