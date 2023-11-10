import json

file_json = r'Password_Manager/data_dicc.json'

# Crear diccionario
data_json = {}

try:
    with open(file_json, 'r') as file:
        data_json = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data_json = {}


def add_data(plat, user, pssw):
    if plat in data_json:
        data_json[plat].append({
            'Usuario: ' : user,
            'Contrasena: ' : pssw
        })
    else:
        data_json[plat] = [{
            'Usuario: ' : user,
            'Contrasena: ' : pssw
        }]

    with open(file_json, 'w') as file:
        json.dump(data_json, file, indent=4)
