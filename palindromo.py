def palindromo(palabra):
    if palabra == palabra[::-1]:
        return "La palabra es un palíndromo"
    else:
        return "No es un palindromo"


def run():
    palabra = input('Escribe una palabra: ').replace(' ', '').lower()
    print(palindromo(palabra))


if __name__ == '__main__':
    run()
