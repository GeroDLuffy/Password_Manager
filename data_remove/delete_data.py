import json
# Ruta al archivo JSON
file_json = r'data_dicc.json'

def rm():
    # Cargar el contenido del archivo JSON en un diccionario
    try:

        with open(file_json, 'R') as file:
            data = json.load(file)

        # Nombre de la plataforma donde esta el usuario que deseas eliminar.
        plat_to_rm = input('Ingrese plataforma: ').capitalize()
        if plat_to_rm in data:
            # Nombre de usuario que deseas eliminar
            user_to_rm = input('Ingrese un usuario que desea eliminar: ')
            if user_to_rm in data[plat_to_rm]:
                confirm = input(f'¿Seguro que quiere borrar el usuario: {user_to_rm}? (Si/No)')
                if confirm.lower() == 'si':
                    del data[plat_to_rm][user_to_rm]
                    # Guardar cambios
                    with open(file_json, 'w') as file:
                        json.dump(data, file, indent=4)
                    print(f'El usuario {user_to_rm} ha sido eliminado.')
                else:
                    print('Eliminacion cancelada.')

            else:
                print(f'El usuario {user_to_rm} no existe en la plataforma {plat_to_rm}')

        else:
            print(f'La plataforma {plat_to_rm} no existe en {data}')



    except FileNotFoundError:
        print(f"El archivo JSON '{file_json}' no existe.")
        return
    except json.decoder.JSONDecodeError:
        print(f"El archivo JSON '{file_json}' no se pudo decodificar correctamente.")    
        return
    
    

    # [key] : [value]






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

