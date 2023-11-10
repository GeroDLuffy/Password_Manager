import json

# Ruta al archivo JSON
file_json = r'Password_Manager/data_dicc.json'

def rm():
    try: 
        # Cargar el contenido del archivo JSON en un diccionario
        with open(file_json, 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        print(f"El archivo JSON '{file_json}' no existe.")
        return
    except json.decoder.JSONDecodeError:
        print(f"El archivo JSON '{file_json}' no se pudo decodificar correctamente.")    
        return
    
    # Nombre de la plataforma donde esta el usuario que deseas eliminar.
    plat_to_rm = input('Ingrese plataforma: ')
    user_to_rm = input('Ingrese un usuario que desea eliminar: ')
    # [key] : [value]

    # Verificar si la plataforma existe en el diccionario.
    if plat_to_rm.capitalize() in data:
        # Verificamos si el usuario existe en el diccionario.
        for us in data[plat_to_rm]:
            if us['Usuario: '] == user_to_rm:
                pass
            else:
                pass
        # data[plat_to_rm] = [user_to_rm]
        




    # # Nombre de la plataforma y usuario que deseas eliminar
    # plataforma_a_modificar = input('Ingrese una plataforma: ')
    # usuario_a_eliminar = input('Ingrese un usuario que desea eliminar: ')

    # # Verificar si la plataforma existe en el diccionario
    # if plataforma_a_modificar in data:
    #     usuarios = data[plataforma_a_modificar]

    #     # Verificar si el usuario que deseas eliminar existe en la plataforma
    #     if usuario_a_eliminar in [item.get('Usuario: ') for item in usuarios]:
    #         # Crear una nueva lista de usuarios sin el usuario a eliminar
    #         nuevos_usuarios = [item for item in usuarios if item.get('Usuario: ') != usuario_a_eliminar]

    #         if not nuevos_usuarios:
    #             # Si no hay usuarios en la plataforma, eliminar la plataforma
    #             del data[plataforma_a_modificar]
    #         else:
    #             # Actualizar la lista de usuarios en la plataforma con la nueva lista
    #             data[plataforma_a_modificar] = nuevos_usuarios

    #         # Guardar el diccionario actualizado en el archivo JSON
    #         with open(file_json, 'w') as file:
    #             json.dump(data, file, indent=4)
    #         print(f"Usuario eliminado de la plataforma {plataforma_a_modificar}: {usuario_a_eliminar}")
    #     else:
    #         print(f"El usuario {usuario_a_eliminar} no existe en la plataforma {plataforma_a_modificar}")
    # else:
    #     print(f"La plataforma {plataforma_a_modificar} no existe en el archivo JSON.")

