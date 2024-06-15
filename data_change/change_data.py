import json
from data_loading.write_Json import add_data

file_json = r'data_dicc.json'

def modify():
    try:
        with open(file_json, 'r') as file:
            data = json.load(file)
            plat = input('Ingrese plataforma a buscar el dato: ').capitalize()
            user = input('Ingrese el usuario a modificar: ')
            # Busca si la plataforma ingresada existe en el diccionario
            if plat in data and user in data[plat]:
                # Lo que puedo hacer acá es hacer una funcion en otro archivo donde en una pide un usuario nuevo y en otra una contraseña nueva
                # Busca si el usuario ingresado existe en la plataforma dentro del diccionario
                pssw = (data[plat][user])
                new_user = input('Ingrese el nuevo usuario: ')
                # Añadimos la key cambiada
                add_data(plat, new_user, pssw)
                # Eliminamos el antiguo usuario
                del data[plat][user]
                
            elif plat not in data:
                print(f'La plataforma: {plat} no existe en el archivo.')
            elif user not in data[plat]:
                print(f'El usuario {user} no existe en la plataforma {plat}')

    except FileNotFoundError:
        print(f"El archivo JSON '{file_json}' no existe.")
    except json.decoder.JSONDecodeError:
        print(f"El archivo JSON '{file_json}' no se pudo decodificar correctamente.")

# import json
# from data_loading.write_Json import add_data

# file_json = r'data_dicc.json'

# def modify():
#     try:
#         with open(file_json, 'r') as file:
#             data = json.load(file)

#             plat = input('Ingrese plataforma a buscar el dato: ').capitalize()
#             # Busca si la plataforma ingresada existe en el diccionario
#             if plat in data:
#                 user = input('Ingrese el usuario a modificar: ')
#                 # Lo que puedo hacer acá es hacer una funcion en otro archivo donde en una pide un usuario nuevo y en otra una contraseña nueva
#                 # Busca si el usuario ingresado existe en la plataforma dentro del diccionario
#                 if user in data[plat]:
#                     new_user = input('Ingrese el nuevo usuario: ')
#                     # Recupera la contraseña del usuario, ya que solo queremos cambiar el usuario
#                     pssw = (data[plat][user])
#                     # Eliminamos el antiguo usuario
#                     del data[plat][user]
#                     # Añadimos la key cambiada
#                     add_data(plat, new_user, pssw)
#                 else:
#                     print(f'El usuario {user} no existe en la plataforma {plat}')
#             else:
#                 print(f'La plataforma {plat} no existe en el archivo {file_json}.')

#     except FileNotFoundError:
#         print(f"El archivo JSON '{file_json}' no existe.")
#     except json.decoder.JSONDecodeError:
#         print(f"El archivo JSON '{file_json}' no se pudo decodificar correctamente.")


    # dicc = {Key : Value}
    # dicc = {[Key] : [Key:Value]}
    # dicc = {[Plataforma : {Usuario:Contrasena}]}
    # data = {[plat]:[user]}
    # data{plat:[{user}]} = [new_user]
    # print(data)
    # plat = input('Ingrese plataforma: ').capitalize()
    # if plat in data:
    #     user = input('Ingrese usuario a cambiar: ')
    #     print(f'{plat}:{data[plat]}')
    #     if user in data[plat]:
    #         print('El usuario existe.')
    #     else:
    #         print(f'El usuario {user} no existe en la plataforma {plat}')
    # else:
    #     print(f'La plataforma {plat} no existe en el diccionario.')


