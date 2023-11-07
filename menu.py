from data_loading.load_data import load
from data_loading.write_Json import add_data
from data_reading.read_Json import read

def options():
    print('\n1. Mostrar todos los usuarios y contraseñas.')
    print('2. Buscar contraseña por usuario.')
    print('3. Agregar un nuevo usuario y contraseña.')
    print('4. Cambiar un usuario.')
    print('5. Cambiar una contraseña.')
    print('6. Salir.')

def main():
    while True:
        options()
        try:
            opt = int(input('Ingrese una opcion: '))      
            if opt >= 1 and opt <= 5:
                if opt == 1:
                    read()
                elif opt == 2:
                    pass
                elif opt == 3:
                    plat, user, pssw = load()
                    add_data(plat, user, pssw)
                elif opt == 4:
                    pass
                elif opt == 5:
                    pass
            elif opt == 6:
                print(' - FIN DEL PROGRAMA - ')
                quit()
            else:
                print('ERROR. Vuelva a ingresar un numero entre 1 y 6: ')
        except ValueError:
            print('Se pidió un NUMERO entre el 1 y el 6.')