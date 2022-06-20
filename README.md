# SquadMakers Reto Python Numero 2

## Requerimientos

La prueba consiste en crear un API Rest en el framework Flask con los siguientes endpoints:
*	Endpoint de chistes. 
o	GET: Se devolverá un chiste aleatorio si no se pasa ningún path param. Si se envía el path param habrá que comprobar si tiene el valor “Chuck” o el valor “Dad”. Si tiene el valor “Chuck” se conseguirá el chiste de este API https://api.chucknorris.io. Si tiene el valor “Dad” se conseguirá del API https://icanhazdadjoke.com/api. En caso de que el valor no sea ninguno de esos dos se devolverá el error correspondiente.
*	Endpoint matemático:
o	GET: Endpoint al que se le pasará un query param llamado “numbers” con una lista de números enteros. La respuesta de este endpoint debe ser el mínimo común múltiplo de ellos.
o	Get: Endpoint al que se le pasará un query param llamado “number” con un número entero. La respuesta será ese número + 1.


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

1. Clonar el repositorio:
`git clone`

2. Crear entorno virtual:
  * Windows:
  Ejecutar en terminal
   * `py -m venv venv`
  * Linux:
   * `python3 -m venv venv`
  * Mac OS:
   * `python3 -m venv venv`
  
3. Iniciar el entorno virtual:
  * Windows:
   * `.\venv\Scripts\activate.bat`
  * Linux:
   * `source ./venv/bin/activate`
  * Mac OS:
   * `source ./venv/bin/activate`
  
4. Instalar librerias:
  * `pip install -r requirements.txt`

5. Crea un archivo `.env` y pega las variables de entorno del archivo `.env-example`.

7. Crea base de datos en Postgres con el nombre dado en el archivo `.env` y crea ejecuta en terminal de postgres:
  * `\c {DATABASE}`
  * `CREATE TABLE joke (id serial PRIMARY KEY, description TEXT, type VARCHAR(255));`

6. Cambia las siguientes variables:
* Windows:
  Ejecutar en terminal
   * `set FLASK_ENV=development`
   * `set FLASK_APP=src\entrypoint`
  * Linux\Mac:
   * `export FLASK_ENV=development`
   * `export FLASK_APP=src\entrypoint`
  
5. Iniciar el servidor:
  * `flask run`

## Pre-requisitos 📋

* Python 3

### Construido con 🛠️

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - framework para API's basado en [Flask](https://flask.palletsprojects.com/en/2.0.x/)


### Versionado 📌

Usamos la siguiente [convención](https://www.notion.so/Commit-conventions-0ab0b6cde23b49e5a9c0bbeb73970072).

### Autor ✒️

* **Santiago Salgado** - [GitHub](https://github.com/Santiagonk)