import random


user_option = input('Elige piedra, papel o tijera: ').lower
options = ('piedra', 'papel', 'tijera')
assert user_option in options, "Elegir una de las opciones"
computer_option = random.choice(options)
print(computer_option)

my_dict = {
        "papel": "piedra",
        "tijera": "papel",
        "piedra": "tijera"
        }

if user_option == computer_option:
    print('Empate!')
elif user_option == my_dict[computer_option]:
    print('perdiste!')
else:
    print('ganaste!')

