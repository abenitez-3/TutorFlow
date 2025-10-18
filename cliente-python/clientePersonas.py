import sys
import datetime
import configparser
import requests
from requests.structures import CaseInsensitiveDict
import datetime


def _pretty(obj):
    import json
    try:
        return json.dumps(obj, ensure_ascii=False, indent=2)
    except Exception:
        return str(obj)


#Variables globales para verificacion
api_personas_url_base = None
archivo_config = 'ConfigFile.properties'
# --- NUEVO: timeout por defecto (puede sobreescribirse desde el .properties) ---
TIMEOUT_SEC = 10


def cargar_variables():
    config = configparser.RawConfigParser()
    config.read(archivo_config)

    global api_personas_url_listar, api_personas_url_crear
    api_personas_url_listar = config.get('SeccionApi', 'api_personas_url_listar')
    api_personas_url_crear = config.get('SeccionApi', 'api_personas_url_crear')
    # --- NUEVO: lee timeout si existe ---
    global TIMEOUT_SEC
    if config.has_option('SeccionApi', 'timeout'):
        try:
            TIMEOUT_SEC = config.getint('SeccionApi', 'timeout')
        except Exception:
            TIMEOUT_SEC = 10


def listar():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = { }
    
    
    r = requests.get(api_personas_url_listar, headers=headers, params=datos, timeout=TIMEOUT_SEC)
    if r.status_code == 200:
        try:
            listado = r.json()
            for item in listado:
                print("      " + str(item))
        except ValueError:
            # Si no es JSON, imprime el texto crudo
            print(r.text)
    else:
        print("Error " + str(r.status_code))
        try:
            print(r.json())
        except ValueError:
            print(r.text)


def crear(cedula: int, nombre: str, apellido: str):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {'cedula': cedula, 
             'nombre' : nombre,
             'apellido' : apellido
            }
    
    r = requests.post(api_personas_url_crear, headers=headers, json=datos, timeout=TIMEOUT_SEC)
    if (r.status_code >= 200 and r.status_code < 300):
        # Validar response
        try:
            print(r.json())
        except ValueError:
            print(r.text)
        
    else:
        print("Error " + str(r.status_code))
        try:
            print(r.json())
        except ValueError:
            print(r.text)


#######################################################
######  Procesamiento principal
#######################################################
print("Iniciando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
cargar_variables()

print("Primer listado de personas:")
listar()
print("________________")


print("Crear nueva persona:")
cedula = int(input("Ingrese cedula: "))
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
crear(cedula, nombre, apellido)


print("________________")
print("Segundo listado de personas:")
listar()

print("Finalizando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))