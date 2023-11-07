import json

# Ruta al archivo JSON
file_json = r'Password_Manager/data_dicc.json'

def rm():
    # Cargar el contenido del archivo JSON en un diccionario
    with open(file_json, 'r') as file:
        data = json.load(file)

    # Nombre de la plataforma y usuario que deseas eliminar
    plataforma_a_modificar = input('Ingrese una plataforma: ')
    usuario_a_eliminar = input('Ingrese un usuario que desea eliminar: ')

    # Verificar si la plataforma existe en el diccionario
    if plataforma_a_modificar in data:
        usuarios = data[plataforma_a_modificar]

        # Verificar si el usuario que deseas eliminar existe en la plataforma
        if usuario_a_eliminar in [item.get('Usuario: ') for item in usuarios]:
            # Crear una nueva lista de usuarios sin el usuario a eliminar
            nuevos_usuarios = [item for item in usuarios if item.get('Usuario: ') != usuario_a_eliminar]

            if not nuevos_usuarios:
                # Si no hay usuarios en la plataforma, eliminar la plataforma
                del data[plataforma_a_modificar]
            else:
                # Actualizar la lista de usuarios en la plataforma con la nueva lista
                data[plataforma_a_modificar] = nuevos_usuarios

            # Guardar el diccionario actualizado en el archivo JSON
            with open(file_json, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Usuario eliminado de la plataforma {plataforma_a_modificar}: {usuario_a_eliminar}")
        else:
            print(f"El usuario {usuario_a_eliminar} no existe en la plataforma {plataforma_a_modificar}")
    else:
        print(f"La plataforma {plataforma_a_modificar} no existe en el archivo JSON.")





    # # Cargar el contenido del archivo JSON en un diccionario
    # with open(file_json, 'r') as file:
    #     data = json.load(file)

    # # Nombre de la plataforma y usuario que deseas eliminar
    # plataforma_a_modificar = input('Ingrese plataforma: ')
    # usuario_a_eliminar = input('Ingrese usuario a eliminar: ')

    # # Verificar si la plataforma existe en el diccionario
    # if plataforma_a_modificar in data:
    #     usuarios = data[plataforma_a_modificar]

    #     # Verificar si el usuario que deseas eliminar existe en la plataforma
    #     if usuario_a_eliminar in [item.get('Usuario: ') for item in usuarios]:
    #         # Eliminar el usuario específico de la plataforma
    #         usuarios = [item for item in usuarios if item.get('Usuario: ') != usuario_a_eliminar]

    #         if not usuarios:
    #             # Si no hay usuarios en la plataforma, eliminar la plataforma
    #             del data[plataforma_a_modificar]
    #         else:
    #             # Actualizar la lista de usuarios en la plataforma
    #             data[plataforma_a_modificar] = usuarios

    #         # Guardar el diccionario actualizado en el archivo JSON
    #         with open(file_json, 'w') as file:
    #             json.dump(data, file, indent=4)
    #         print(f"Usuario eliminado de la plataforma {plataforma_a_modificar}: {usuario_a_eliminar}")
    #     else:
    #         print(f"El usuario {usuario_a_eliminar} no existe en la plataforma {plataforma_a_modificar}")
    # else:
    #     print(f"La plataforma {plataforma_a_modificar} no existe en el archivo JSON.")










# import json

# file_json = r'Password_Manager/data_dicc.json'

# def rm():
#     with open(file_json, 'r') as file:
#         data = json.load(file)

#     choose_plat = input('Ingrese la plataforma: ')
#     choose_user = input('Ingrese usuario que desea eliminar: ')

#     if choose_plat.capitalize() in data and choose_user in [item.get('Usuario: ') for item in data[choose_plat.capitalize()]]:
#         data[choose_plat.capitalize()] = [item for item in data[choose_plat.capitalize()] if item.get('Usuario: ') != choose_user]

#         with open(file_json, 'w') as file:
#             json.dump(data, file, indent=4)

#         print(f'Usuario eliminado de la plataforma {choose_plat}: {choose_user}')
#     else:
#         print(f'No existe la plataforma: "{choose_plat}" y/o usuario: "{choose_user}".')
