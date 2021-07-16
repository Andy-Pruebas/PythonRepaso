'''
    EjercicioIf
'''
n1=int(input('Ingresar el primer numero'))
n2=int(input('Ingresar el segundo numero'))

if n1%2==0 and n2%2==0:
    print('ambos numeros son pares')
elif n1%2==0 and n2%2!=0:
    print(f'el numero {n1} es par')
elif n1%2!=0 and n2%2==0:
    print(f'el numero {n2} es par')
else:
    print('ninguno es par')