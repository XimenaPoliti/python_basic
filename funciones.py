#def imprimir_mensaje():
#    print('¡Hola!')

def conversacion(opcion):
    print(f""" 
    ¡Hola! ¿Cómo estás?
    Elegiste la opcion {opcion}
    ¡Adios!""")

opcion = int(input('Por favor elige una opcion(1, 2, 3): '))

if 4 > opcion > 0:
    conversacion(opcion)
else:
    print('Por favor, seleccione una de las opciones disponibles')



