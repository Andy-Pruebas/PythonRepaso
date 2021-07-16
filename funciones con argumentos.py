'''Argumento nulo'''
#def nulo(x=None,y=None):
#    if x == None or y == None:
#        print("Ingrese los 2 valores ")
#        return
#    return x/y
#print(nulo())

'''Funciones con variables'''
#def estudiante(valor):
#       valor*3
#variable=15
#print(variable)
'''lista'''
#def listas(numero):
#    for x,i in enumerate(numero):
#        numero[x]*=3
#lista=[50,100,150]
#listas(lista[:])
#print(lista)

#def estudiante(valor):
#    return valor*3
#variable=15
#variable=estudiante(variable)
#print(variable)
'''Argumentos indeterminados'''
'''posicion'''
#def argu(*tu):
#    for tus in tu:
#        print(tus)
#argu('Andy','Vilca',20,30,{1,2,3})
'''nombre'''
#def nombre_dicc(**dicc):
#    for x in dicc:
#        print(x," ",dicc[x])
#nombre_dicc(Andy='Vilca',Programador='Python',notas={19,20,18})
'''Funcion combinada'''
#def nombre_dicc(*tu,**dicc):
#    a=0
#    for tus in tu:
#        a+=tus
#        print(a)
#    for x in dicc:
#        print(x," ",dicc[x])
#nombre_dicc(1,2,3,4,5,Andy='Vilca',Programador='Python',notas={19,20,18})

