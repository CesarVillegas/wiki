from django.shortcuts import render
import markdown

from . import util


# Vista para la página de índice que lista todas las entradas de la enciclopedia
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Vista para mostrar una entrada específica de la enciclopedia
def entrada(request, title):
    doc = util.get_entry(title)
    
    if doc == None:
        # Si el documento no existe, mostrar página de error
        return render(request, "encyclopedia/error.html", {"title": title}) 
    
    # Si el documento existe, convertirlo a HTML
    doc_html = markdown.markdown(doc)

    return render(request, "encyclopedia/entrada.html", {"doc": doc_html, "title": title})


# Vista para manejar la búsqueda de entradas en la enciclopedia
def busqueda(request):
    if request.method == "POST":
        # validar parametro q
        consulta = request.POST.get("q", "")
        texto_busqueda = consulta.lower()
        # Obtener todos los nombres de las entradas de la enciclopedia
        entradas = util.list_entries()

        # Buscar entradas que coincidan exactamente con la consulta
        for entry in entradas:
            entry_minuscula = entry.lower()
            if texto_busqueda == entry_minuscula:
                return entrada(request, entry)  


        # Buscar todas las entradas que contengan la consulta
        entradas_encontradas = []
        for entry in entradas:
            entry_minuscula = entry.lower()

            # Verificamos si la consulta está dentro de la entrada
            if texto_busqueda in entry_minuscula:
                entradas_encontradas.append(entry)
        
        return render(request, "encyclopedia/resultados-busquedas.html", {
            "consulta": consulta,
            "entradas": entradas_encontradas
        })
    
    # Si no es un POST, redirigir al índice
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })