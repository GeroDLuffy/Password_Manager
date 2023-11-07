from menu import main

def master_pssw():
    master = 'contrasena'
    tries = 3
    while True:
        attempt = input('Ingrese la contraseña maestra: ')
        if attempt.lower() == master:
            main()
        else:
            if tries == 1:
                print(' - FIN DEL PROGRAMA - ')
                quit()
            else:
                tries -= 1
                print(f'Error, contraseña incorrecta. Tenes {tries} intentos más.')
master_pssw()
