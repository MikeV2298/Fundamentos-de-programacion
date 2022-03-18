

print('<< PLANTAS ENERGÉTICAS >> \n')
def saludo(nombre):
    
    print('Hola {}'.format(nombre),', bienvenido.\n')
    
x = input('Ingrese su nombre: ')
saludo(x)

consumo_energia = {
    'Coca Codo Sinclair':{
        'Isla San Crtbl': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84}
        
    
    },
    
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Manta': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32}
    },
}

plantas = {
    'Quito': ('Coca Codo Sinclair', 'Sopladora'),
    'Guayaquil': ('Coca Codo Sinclair', 'Sopladora'),
    'Isla San Crtbl': ('Coca Codo Sinclair'), 
    'Loja': ('Sopladora'),
    'Tena': ('Sopladora'),
    'Manta': ('Sopladora')
}

informacion = {
    'Costa': ('Guayaquil', 'Manta'),
    'Sierra': ('Quito', 'Ambato', 'Loja'),
    'Oriente': ('Tena', 'Nueva Loja'),
    'Insular': ('Isla San Crtbl')
}

def total_consumo_por_planta_ciudad(planta, ciudad):
    if planta not in consumo_energia.keys():
        return 'La planta ' + planta + ' no existe'

    if ciudad not in consumo_energia[planta].keys():
        return 'La planta ' + planta + ' no proveé energía a la ciudad de ' + ciudad

    total_consumo = sum(consumo_energia[planta][ciudad]['consumos'])
    return total_consumo

def ciudad_plantas():
    for llaves in plantas:
        if ciudad in llaves:
            for llaves in consumo_energia['Coca Codo Sinclair']:
                if llaves == ciudad:
                    total_coca = (sum(consumo_energia['Coca Codo Sinclair']['{}'.format(ciudad)]['consumos']))
                    print('Coca Codo Sinclair: ',total_coca, 'MWh')
                    continue
            for llaves in consumo_energia['Sopladora']:
                if llaves == ciudad:
                    total_sopladora = (sum(consumo_energia['Sopladora']['{}'.format(ciudad)]['consumos']))        
                    print('Sopladora: ',total_sopladora, 'MWh')
        if ciudad not in plantas:
            print ('La ciudad que ingreso no cuenta con registros')
            break

def recaudacion ():
    ciudades_region = informacion[region]
    total_consumo = 0
    
    for ciudad_region in ciudades_region:
        for planta in consumo_energia.keys():
            for ciudad in consumo_energia[planta].keys():
                if ciudad_region == ciudad:
                    total_consumo += sum(consumo_energia[planta][ciudad]['consumos'])*consumo_energia[planta][ciudad]['tarifa']
    print(region, ':','$', total_consumo '\n')


op = -1
while op != 0:
    print("ESCOJA UNA OPCIÓN DISPONIBLE:")
    print('<1> Total de MWH por dicha Planta y Ciudad.')
    print('<2> Total de MWH por cada Planta')
    print('<3> Total de dinero recaudado por cada región')
    print('<0> SALIR \n')
      

    op = int(input('Ingrese opción: '))

    while op == 1:
        print()
        print('Plantas que proveen energía: Coca Codo Sinclair / Sopladora \n')
        
        planta = input('Ingrese el nombre de la planta: ')
        ciudad = input('Ingrese el nombre de la ciudad que desee consultar: ')

        total = total_consumo_por_planta_ciudad(planta, ciudad)

        if type(total) == int:
            print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total, planta))
        else:
            print(total)
        print('¡VOLVIENDO AL MENU PRINCIPAL!')
        break
    while op == 2:
        ciudad =  input('Ingrese el nombre de la ciudad: ')
        ciudad_plantas()
        print('¡VOLVIENDO AL MENU PRINCIPAL!')
        break
    while op == 3:
        region = input('Region: ')
        if region not in informacion.keys():
            print ('¡La region que busca no existe!')
            print('¡VOLVIENDO AL MENÚ PRINCIPAL!')
            break
        if region in informacion.keys():
            recaudacion()
            print('¡VOLVIENDO AL MENÚ PRINCIPAL!')
            break
