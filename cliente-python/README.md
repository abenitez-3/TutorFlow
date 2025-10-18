
********************************************
Pasos para ejecutar el proyecto
********************************************

Paso 1) Descargar del GIT

Paso 2) Instalar Python3

Paso 3) Instalar Pip3

Paso 4) Ejercutar el comando:
    pip3 install requests

Paso 5) Configurar el archivo de configuración.
Existe un archivo de configuración "ConfigFile.properties"
Allí se configura las URL que el cliente Python usa

Paso 6) Ejecutar el programa:
    python clientePersonas.py

# Cliente Python (Personas)

## Requisitos
- Windows 10/11, Python 3.x.
- Servidor backend con endpoints de Personas:
  - GET    {BASE_URL}{PERSONAS_ENDPOINT}
  - GET    {BASE_URL}{PERSONAS_ENDPOINT}/{id}
  - POST   {BASE_URL}{PERSONAS_ENDPOINT}
  - PUT    {BASE_URL}{PERSONAS_ENDPOINT}/{id}
  - DELETE {BASE_URL}{PERSONAS_ENDPOINT}/{id}

## Configuración
Edita `ConfigFile.properties`: