cambio = [3875, 4383, 58800, 136134100] 
cifras = [2,2,4,9]
monedas = ['dolares', 'euros', 'cakes', 'bitcoins']
mensaje = '''
¡Bienvenido al conversor de monedas!

    Te brindamos las siguientes opciones:
    1. Dolares
    2. Euros
    3. Cake
    4. Bitcoins

Por favor, ingrese la opción requerida: '''

def get_change(opcion, peso_colombiano):
    resultado = round((peso_colombiano / cambio[opcion - 1]), cifras[opcion - 1]) 
    print(f"""Tienes: {resultado} {monedas[opcion - 1]}""")

opcion = int(input(mensaje))
if 5 > opcion > 0:
    peso_colombiano = float(input('ingrese la cantidad a convertir: '))
    get_change(opcion, peso_colombiano)
else:
    print('Opción ingresada no es válida')

  
#if mi_opcion == 1:
#    dolar = round((peso_colombiano / 3875), 2)   
#    print("Tienes $", dolar , " dolares")
#elif mi_opcion == 2:         
#    euro =  round((peso_colombiano / 4383), 2)
#    print("Tienes $", euro , " Euros")  
#elif mi_opcion == 3:
#    cake =  round((peso_colombiano / 58800), 4)
#    print("Tienes: ", cake , " CAKE") 
#elif mi_opcion == 4:
#    bitcoin =  round((peso_colombiano / 136134100), 9)
#    print("Tienes: " , bitcoin , " Bitcoins")
#else:
#    print('Opción ingresada no es válida')

