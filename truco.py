import random
 


# definir las cartas del mazo

palo = ['oro', 'copas', 'espadas', 'bastos']
numeros = [1,2,3,4,5,6,7,10,11,12]

# crear el mazo de cartas

mazo_naipes = [(n,p) for n in numeros for p in palo]
# for carta in mazo_naipes:
    # print (f'{carta[0]} de {carta[1]}')
# print(f'tipo de carta {type(carta)}')


# funcion para repartir las cartas

def repartir_cartas(mazo, num_jugadores):
    cartas_jugadores = []
    for _ in range(num_jugadores):
        cartas_jugador = random.sample(mazo,3)
        cartas_jugadores.append(cartas_jugador)
        # for carta in cartas_jugador:      estas lineas eleiminan del mazo, las cartas que se repartieron.
        #     mazo.remove(carta)            
        # print('el mazo que asi\n', mazo)
    return cartas_jugadores


# def escala_valor():
#     valores = [34, 20, 30, 40, 50, 60,]
#     rango_max = 100
#     rango_min = 0
#     escala = [(x - min(valores))/(max(valores) - min(valores)) * (rango_max - rango_min) + rango_min for x in valores]
#     return escala


# funcion determina el valor de las cartas

def determinar_valor_carta(carta_jugador_1,carta_jugador_2):
    
    escala_valor = {'1 espadas': 1, '1 bastos': 2, '7 espadas': 3, '7 oro': 4, '3 oro': 5, '3 copas': 5, '3 bastos': 5, '3 espadas': 5, 
                    '2 oro': 6, '2 copas': 6, '2 bastos': 6, '2 espadas': 6, '1 oro': 7, '1 copas': 7, '12 oro': 8, '12 copas': 8,
                     '12 bastos': 8, '12 espadas': 8, '11 oro': 9, '11 copas': 9,'11 bastos': 9, '11 espadas': 9, '10 oro': 10, '10 copas': 10,
                     '10 bastos': 10, '10 espadas': 10, '7 copas': 11, '7 bastos': 11, '6 oro': 12, '6 copas': 12, '6 bastos': 12, '6 espadas': 12,
                     '5 oro': 13, '5 copas': 13, '5 bastos': 13, '5 espadas': 13, '4 oro': 14, '4 copas': 14, '4 bastos': 14, '4 espadas': 14}
    valor_1 = escala_valor[carta_jugador_1]
    valor_2 = escala_valor[carta_jugador_2]
    if valor_1 > valor_2:
        gana = 'jugador_2'
    elif valor_2 > valor_1:
        gana = 'jugador_1'
    else:
        gana = 0
    return gana
    
    # print (type(valor_1))
    # print (type(valor_1))
    # print (f'el valor de la carta es {valor_1}')
    # print (f'el valor de la carta es {valor_2}')
    # print (f'diccionario {escala_valor}')



# funcion para repartir las cartas

def jugar_truco():
    # jugadores = 2
    jugador_1 = []
    jugador_2 = []
    partida_1 = repartir_cartas(mazo_naipes, 2)
    print(f'vista de       {partida_1}\n')
    # print(type(partida_1))
    for i, cartas in enumerate(partida_1):
        # print(f'Jugador {i+1}:{cartas}')
        # print(f'{cartas}\n')
        if i == 0:
            jugador_1 = cartas
        else:
            jugador_2 = cartas
    return jugador_1, jugador_2   

# funcion para determinar la clave de la carta

def carta_de_la_mano(_carta):
    aux = ''
    aux += str(_carta[0])
    aux += ' '
    aux += str(_carta[1])
    # for i in _carta:
    #     print (f'eñ indice es {i}')
    #     aux += _carta[i-1] + ''
    # ''''aux = ','.join(_carta)''''
    # print (type(_carta))
    return aux
        

# principal del juego

print('-' * 50)
print('Jugar una mano de truco\n')
print('Para jugar una carta presione:\n1- Primer carta\n2- Segunda carta\n3- Tercer carta\n')
opcion = ''
# cont = 0
cont_jug_1 = 0
cont_jug_2 = 0

while opcion != 'n':
    condicion_parda = False
    print('-' * 50)
    opcion = input(('S. jugar..\nN. salir\n'))
    # print('-' * 30)
    if opcion == 's':
        jugador_1, jugador_2 = jugar_truco()
        # print (f'Sus cartas son: {jugador_1}\n')
        print('-' * 50)
        for i in range(3):
             # cont -= 1
            print (f'Sus cartas son: {jugador_1}\n\n')
            # print ('mis cartas: ', jugador_2)
            print('Ud es mano...\n' if i == 0 else '')
            carta_jug_1 = int(input('Juegueee!!!!\n'))       
            aux_jug_1 = jugador_1[carta_jug_1 - 1]
            # print(type(aux_jug_1))
            print(f'Jugaste el    {aux_jug_1}\n')
            jugador_1.pop(carta_jug_1 - 1)
            aux_jug_1 = carta_de_la_mano(aux_jug_1)
            aux_jug_2 = jugador_2[i]
            print(f'Mi carta es   {aux_jug_2}\n' )
            # jugador_2.pop(i)
            aux_jug_2 = carta_de_la_mano(aux_jug_2)
            ganador = determinar_valor_carta(aux_jug_1, aux_jug_2)

            # en pardas si uno gana la segunda termina el juego
            if  condicion_parda == True and i == 1 and ganador == 'jugador_1':
                cont_jug_1 += 1
                break
            elif condicion_parda == True and i == 1 and ganador == 'jugador_2':
                cont_jug_2 += 1
                break
            # print(f'condicional {condicion_parda},  i {i},  ganador {ganador}')

            if ganador == 'jugador_1'and i == 0:
                cont_jug_1 += 1
                print('Esta de suerte hiciste primera\n')
            elif ganador == 'jugador_1' and i == 1:
                cont_jug_1 += 1
                print('Hiciste segunda\n')
            elif ganador == 'jugador_1' and i == 2:
                cont_jug_1 += 1
                print('Ganaste tercera\n')
            elif ganador == 'jugador_2' and i == 0:
                cont_jug_2 += 1
                print ('Yo hice primera, jejeje\n')
            elif ganador == 'jugador_2' and i == 1:
                cont_jug_2 += 1
                print ('Hice segunda\n')
            elif ganador == 'jugador_2' and i == 2:
                cont_jug_2 += 1
                print ('Hice tercera\n')
            elif cont_jug_1 == 0 and cont_jug_2 == 0:
                print('Es parda, va la mejor.....\n' if i == 0 else '')
                print('Sigue parda!!!...\n' if i == 1 else '')
                condicion_parda = True
                # print(condicion_parda)
        
        if cont_jug_1 > cont_jug_2:
            print('Ganaste esta mano!!!')
        elif cont_jug_2 > cont_jug_1:
            print('Te gane esta mano!!!!!!!!!!!')

        # print(aux_2)
        
        # determinar_ganador(aux_1, jugador_2)

       # print (f'{jugador_2}\n')
    elif opcion == 'n':
        print('Chauu cobarde!!')
    else:
        print("Ingrese una opcion valida... ")
        
   



# ganador = determinar_ganador(aux_1, jugador_2)

# print(f'ganador {ganador}')





# di
# Diego Vargas
# 21:40
# class Bici():
# ruedas = 2

# def __init__(self, marca, color):
# self.marca = marca
# self.color = color


# bici_olmo_1 = Bici('Olmo', 'Gris')


# print(f'El color del marco de la bici es: {bici_olmo_1.color}')
# print(f'La marca del marco de la bici es: {bici_olmo_1.marca}')
# print(f'La cantidad de ruedas es: {bici_olmo_1.ruedas}')


