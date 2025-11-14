# Léeme 

## Creación de entorno para proyecto Wiki

* Se crea y activa entorno virtual de python llamado **venv_wiki**
* Se crea proyecto django llamado wiki
* Se descarga código inicial del project1 wiki del curso.
* Se crea archivo de requerimientos del proyecto (requirements.txt)


## Implementando la encyclopedia "wiki"

### Requerimientos Entry Page: 
* Se utiliza función get_entry() del archivo util.py para recuperar una enciclopedia por su título.
* Si una entrada no existe se genera un archivo error (wiki/encyclopedia/templates/encyclopedia/error.html)
* Se crea página para mostrar el contenido de la entrada, para correcta visualización del contenido se instala librería (incluida en archivo requirements.txt) para transformar archivos MD (Markdown a HTML) a html y asi visualizar la entrada en la página.

