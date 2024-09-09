from random import *

nombre = input('Ingrese su nombre: ')
numero = 0

print(f'{nombre} he pensado un número entre el 1 y el 100, tienes que adivinarlo en 8 intentos')

numero_aleatorio = randint (1, 100)

while numero >= 0:
    numero += 1
    res = input('Intento numero '+str(numero)+': ')
    res2 = int(res)

    if numero == 8:
        print("Perdiste, no lograste adivinar el numero")
        break
    elif res2 < 0 or res2 > 100:
        print("Valor incorrecto, inserta un valor entre 1 y 100\n")
        numero -= 1
        continue
    elif res2 < numero_aleatorio:
        print("Ingresa un numero mas grande\n")
        continue
    elif res2 > numero_aleatorio:
        print("Ingresa un número menor\n")
        continue
    elif numero_aleatorio == res2:
        print(f"\nFelicidades {nombre} ganaste!!! El número aleatoria es: {numero_aleatorio}")
        if numero == 1:
            print(f"Te costo solo 1 intento")
        else:
            print(f"Te costo solo {numero} intentos")
        break
