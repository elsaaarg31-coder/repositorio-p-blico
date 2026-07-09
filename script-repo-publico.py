#comentario
from pathlib import Path

# Selecciona la carpeta actual
carpeta_actual = Path('.')

# Lista solo los ficheros (ignora las carpetas)
for archivo in carpeta_actual.iterdir():
    if archivo.is_file():
        print(archivo.name)