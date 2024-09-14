# Pasos para ejecutar el proyecto

Es necesario clonar el proyecto a través de la URL
https://github.com/Complejidad-Algoritmica/backend-python.git

1. (Por única vez) Abrir la terminal, crear el entorno virtual para python:
    comando: python -m venv venv
2. (Cada vez que quieras instalar nuevas dependencias) Activar el entorno virtual:
    comando (desde la raíz): cd venv\Scripts
    comando: activate
3. (Por primera vez) Regresar a la raíz con:
    comando: cd ../..
    Instalar las dependencias del .txt:
    comando: pip install -r requirements.txt
    *debes estar en la raíz del proyecto*
4. Levantar backend:
    comando: uvicorn src.main:app --reload
5. Codear en el único endpoint :D

**opcional**
si se instalarán nuevas librerías utilizar comando con el entorno activado:
pip install *libreria_nombre*
y utilizar el comando:
pip freeze > requirements.txt
esto para que todos tengamos las mismas librerias

