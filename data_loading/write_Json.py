import json
import os

file_json = r'Password_Manager/data_dicc.json'
# Crear diccionario
data_json = {}
data_json['info'] = []

def add_data(plat, user, pssw):
    data_json['info'].append({
        'Plataforma: ' : plat,
        'Usuario: ' : user,
        'Contrasena: ' : pssw
    })
    with open(file_json, 'w') as file:
        json.dump(data_json, file, indent=4)


    # if os.path.exists(file_json):
    #     with open(file_json, 'a') as file:
    #         json.dump(data_json, file, indent=4)
    # else:
    #     with open(file_json, 'w') as file:
    #         json.dump(data_json, file, indent=4)
