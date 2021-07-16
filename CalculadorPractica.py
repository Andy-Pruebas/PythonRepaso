print("Escoge tu opción")
inicio= str(input("Ingresar una opción: "))
while (inicio == 'empezar'):
    print("""¿Que opción eligiras?
    Escribe una opción
    1 - Quiero sumar
    2 - Quiero restar
    3 - Quiero multiplicar
    4 - Quiero dividir
    5 - Salir de las opciones """)
    opcion = input()
    if opcion == '1':
        print("Suma")
        n1=int(input("Ingresar el primer numero"))
        n2=int(input("Ingresar el segundo numero"))
        suma=n1+n2
        print(suma)
    elif opcion == '2':
        print("Resta")
        n1=int(input("Ingresar el primer numero"))
        n2=int(input("Ingresar el segundo numero"))
        resta=n1-n2
        print(resta)
    elif opcion == '3':
        print("Multiplicar")
        n1=int(input("Ingresar el primer numero"))
        n2=int(input("Ingresar el segundo numero"))
        multiplicacion=n1*n2
        print(multiplicacion)
    elif opcion == '4':
        print("Dividir")
        n1=int(input("Ingresar el primer numero"))
        n2=int(input("Ingresar el segundo numero"))
        dividir=n1/n2
        print(dividir)
    else:
        print("Gracias por usar la aplicacion")
        break