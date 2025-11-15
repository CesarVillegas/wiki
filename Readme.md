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
    git checkout main
    git merge IndexPage
    git push origin main


#### Search:

* Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
* If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
* If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.
* Clicking on any of the entry names on the search results page should take the user to that entry’s page.

~~~mermaid
flowchart TD
    Z((Inicio)) --> A["Ingresar búsqueda"]
    A --> B{"¿La búsqueda coincide exactamente con una entrada?"}
    B -- Sí --> C["Redirigir a la entrada correspondiente"]
    B -- No --> D{"¿La búsqueda coincide parcialmente con alguna entrada?"}
    D -- Sí --> E["Mostrar lista de resultados coincidentes"]
    E --> |Click| C["ir a la entrada"]
    D -- No --> F["Mostrar mensaje: 'No se encontraron resultados'"]
    C --> H((Fin))
    F --> H
~~~



Se incorpora una clase forms de django en el layout del proyecto para realizar las búsquedas, utilizando asi validaciones del lado del cliente y servidor.