import json
# Crear diccionario
data_json = {}

def add_data(plat, user, pssw):
    data_json['info'] = ({
        'Plataforma: ' : plat,
        'Usuario: ' : user,
        'Contrasena: ' : pssw
    })

    with open( r'Password_Manager/data_dicc.json', 'w') as file:
        json.dump(data_json, file, indent=4)
