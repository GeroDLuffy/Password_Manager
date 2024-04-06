import json
file_json = r'data_dicc.json'

# Intenta cargar el contenido del archivo JSON
def read():
    try:
        with open(file_json, 'r') as file:
            data = json.load(file)

            # Recorre el diccionario y muestra cada clave y valor
            for plataform, info in data.items():
                print("\nPlataforma:", plataform)
                for user, pssw in info.items():
                        print(f'Usuario: {user}')
                        print(f'Contraseña: {pssw}')
                        print()  # Línea en blanco entre los elementos

    except FileNotFoundError:
        print(f"El archivo JSON '{file_json}' no existe.")
    except json.decoder.JSONDecodeError:
        print(f"El archivo JSON '{file_json}' no se pudo decodificar correctamente.")
