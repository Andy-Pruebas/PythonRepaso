'''
Ejercicio1.py
'''
print('Repaso con Python')
calcular=str(input("Ingresar una opción: "))
while (calcular == 'calcular'):
    print("""
    ¿Que opción escogeras?
    Elige una opcion
    1 - Calcular con formula
    2 - Salir
    """)
    opcion = input()
    if opcion == '1':
        a=float(input('Ingrese el valor para a:'))
        b=float(input('Ingrese el valor para b: '))
        c=float(input('Ingrese el valor para C:'))

        r=((c+5)*(b**2-3*a*c)*a**2)/(4*a)
        print (f'el resulado del calculo por fomular es: {r}')
    else:
        print('Gracias por usar la aplicación')
        break

