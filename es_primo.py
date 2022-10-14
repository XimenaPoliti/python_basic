def es_primo(numero):
    if numero == 1:
        return False

    for contador in range(2,numero):
        if numero % contador != 0:  # no es divisible
            continue
        return False                # no es primo
    return True                     # es primo


def run():
    numero = int(input('Por favor, escribe un número: '))
    if es_primo(numero):
        print(f'El número {numero} es primo')
    else:
        print(f'El número {numero} no es primo')

if __name__ == '__main__':
    run()
