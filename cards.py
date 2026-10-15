def crear_baraja():
    #picas=0; corazon=1; diamantes=2; treboles=3; 
    baraja = []
    for y in range(4):
        for x in range(1,8):
            tuple=(x, y)
            baraja.append(tuple)
        baraja.append(('J',y))
        baraja.append(('Q',y))
        baraja.append(('K',y))
    return baraja
#print(crear_baraja())

def obtener_valor(carta):
    pass


def obtener_palo(carta):
    pass


def mismo_valor(carta1, carta2):
    pass


def misma_carta(carta1, carta2):
    pass


def validar_baraja(baraja):
    pass


def mezclar_baraja(baraja):
    pass


def repartir_cartas(baraja, cantidad):
    pass


def repartir_dos_jugadores(baraja):
    pass