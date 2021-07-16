'''
    EjercicioIF3.py
'''
nom1=str(input('nombre 1 : '))
nom2=str(input('nombre 2 : '))

if nom1[0] == nom2[0] or nom1[-1] == nom2[-1]:
    print('Si hay Coincidencia')
else:
    print('No hay Coincidencia')
