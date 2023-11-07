import json
file_json = r'Password_Manager/data_dicc.json'

# Intenta cargar el contenido del archivo JSON
def read():
    try:
        with open(file_json, 'r') as file:
            data = json.load(file)

            # Recorre el diccionario y muestra cada clave y valor
            for plataforma, informacion in data.items():
                print("\nPlataforma:", plataforma)
                for item in informacion:
                    for clave, valor in item.items():
                        print(f"{clave}: {valor}")
                    print()  # Línea en blanco entre los elementos

    except FileNotFoundError:
        print(f"El archivo JSON '{file_json}' no existe.")
    except json.decoder.JSONDecodeError:
        print(f"El archivo JSON '{file_json}' no se pudo decodificar correctamente.")
