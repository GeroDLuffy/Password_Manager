import json

file_json = r'data_dicc.json'

# Crear diccionario
data_json = {}

try:
    with open(file_json, 'r') as file:
        data_json = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data_json = {}


def add_data(plat, user, pssw):
    # Si existe la plataforma en el archivo, añadirla debajo de esa misma
    if plat in data_json:
        data_json[plat][user] = pssw
    else:
    # Si no, añadir el archivo de la misma forma que los otros
        value = {user:pssw}
        data_json[plat] = (value)

    # Escribir la info en el archivo json
    with open(file_json, 'w') as file:
        json.dump(data_json, file, indent=4)

