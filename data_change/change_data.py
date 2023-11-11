import json
from data_loading.write_Json import add_data

file_json = r'Password_Manager/data_dicc.json'

def algo():
    try:
        with open(file_json, 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        print(f"El archivo JSON '{file_json}' no existe.")
    except json.decoder.JSONDecodeError:
        print(f"El archivo JSON '{file_json}' no se pudo decodificar correctamente.")

    # dicc = {Key : Value}
    # dicc = {[Key] : [Key:Value]}
    # dicc = {[Plataforma : {Usuario:Contrasena}]}
    # data = {[plat]:[user]}
    # data{plat:[{user}]} = [new_user]
    # print(data)
    plat = input('Ingrese plataforma: ').capitalize()
    if plat in data:
        user = input('Ingrese usuario a cambiar: ')
        print(f'{plat}:{data[plat]}')
        if user in data[plat]:
            print('El usuario existe.')
        else:
            print(f'El usuario {user} no existe en la plataforma {plat}')
    else:
        print(f'La plataforma {plat} no existe en el diccionario.')

