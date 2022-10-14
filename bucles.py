def potencia(numero, numero_maximo):
    potencia = 0
    resultado = 0
    while numero_maximo > resultado:
        print(f'{numero} elevado a {potencia} es: {resultado}')
        potencia +=1
        resultado = numero**potencia 


def run():
    numero = int(input('Ingrese el número al cuál quieres averiguar la potencia: '))
    numero_maximo = int(input('Ingrese el límite de la potencia: '))
    potencia(numero, numero_maximo)
    

if __name__ == '__main__':
    run()
