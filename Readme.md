# Léeme 

## Creación de entorno para proyecto Wiki

* Se crea y activa entorno virtual de python llamado **venv_wiki**
* Se crea proyecto django llamado wiki
* Se descarga código inicial del project1 wiki del curso.
* Se crea archivo de requerimientos del proyecto (requirements.txt)


## Implementando requerimientos encyclopedia "wiki":

#### Entry Page: 
* Se utiliza función get_entry() del archivo util.py para recuperar una enciclopedia por su título.
* Si una entrada no existe se genera un archivo error (wiki/encyclopedia/templates/encyclopedia/error.html)
* Se crea página para mostrar el contenido de la entrada, para correcta visualización del contenido se instala librería (incluida en archivo requirements.txt) para transformar archivos MD (Markdown a HTML) a html y asi visualizar la entrada en la página.

#### Index Page: 
Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.

* Se implementa funcionalidad href para las entradas de la enciclopedia.
* Se aprovecha de crear la variable app_name para evitar conflictos futuras aplicaciones que tengan mismo name en urls, ejemplo index.
* Se crea una rama de git para generar esta funcionalidad.

    git add *
    git commit -m "mensaje"
    git push origin IndexPage
    git checkout -b IndexPage
    