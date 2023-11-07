def load():
    platform = input('Ingrese plataforma: ')
    users = input('Ingrese usuario: ')
    password = input('Ingrese contraseña: ')
    print('¡Se agregaron con exito los datos!')
    return platform.capitalize(), users, password
