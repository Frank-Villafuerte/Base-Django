Crear un entorno virtual
Usando virtualenv:
Instalar virtualenv (si no lo has hecho ya):

bash
Copy code
pip install virtualenv
Crear un nuevo entorno virtual:

En la terminal, navega al directorio donde desees crear el entorno y ejecuta:

bash
Copy code
virtualenv nombre_entorno
Activar el entorno virtual:

En Windows:

bash
Copy code
nombre_entorno\Scripts\activate
En macOS y Linux:

bash
Copy code
source nombre_entorno/bin/activate
Instalar dependencias desde requirements.txt
Una vez que tienes tu entorno virtual activo, puedes instalar las dependencias desde un archivo requirements.txt.

Si tienes un archivo requirements.txt:
Ubícate en el directorio donde está tu archivo requirements.txt y activa tu entorno virtual.

Instala las dependencias desde el archivo requirements.txt:

bash
Copy code
pip install -r requirements.txt
Esto instalará todas las dependencias listadas en requirements.txt en tu entorno virtual activo.
