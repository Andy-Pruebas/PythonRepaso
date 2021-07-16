'''Excepciones'''
#while(True):
#    try:
#        variable = int(input("Ingresa un numero"))
#        a=2
#        print("Resultado: ",a*variable)
#    except:
#        print("Colocaste otro tipo de valor que no es numerico")
#    else:
#        print("Iniciaste sesión")
#        break
'''Excepciones multiples e invocaciones'''
try:
    a=float(input("Numero: "))
    b=10/a
    print(b)
except TypeError:
    print("Esto es texto")
except ValueError:
    print("El valor ingresado debe ser un numero")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except Exception as x:
    print(type(x).__name__)
