'''
    EjercicioIF4.py
'''
print('Cajero Automatico Python')
saldo=2000
passw=int(input('Ingrese su cuenta bancaria'))
while (passw == 3844556677):
    print("""
    Opciones del cajero
    1 - Ingresar dinero
    2 - Retirar dinero
    3 - Mostrar dinero
    4 - salir    
    """)
    opcion=input()
    if opcion == '1':
        print('Ingresar un monto de dinero')
        ingreso=float(input('cantidad a ingresar en la cuenta'))
        saldo+=ingreso
        print(f'se agregaron {ingreso} a la cuenta y el saldo es de {saldo}')
    elif opcion == '2':
        print('Retirar monto de dinero')
        retiro=float(input('ingresar la cantidad a retirar'))
        if retiro>saldo:
            print('saldo insuficiente')
        else:
            saldo -= retiro
            print(f'Se retiraron {retiro} y el saldo actual es de {saldo}')
    elif opcion == '3':
        print('Mostrar la cantidad de dinero en la cuenta')
        print(f'saldo actual {saldo}')
    elif opcion == '4':
        print("Gracias por realizar sus transacciones")
        break
    else:
        print("ingreso una opcion invalida")

