import random

def adivina(numero, random):
    while numero != random:
        if numero < random:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero =  int(input('Elige otro número: '))   
    print('¡Ganaste!')


def run():
    aleatorio = random.randint(1,100)
    numero =  int(input('Elige un número del 1 al 100: '))
    adivina(numero, aleatorio)


if __name__ == '__main__':
    run()
