from django.shortcuts import render
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entrada(request, title):
    doc = util.get_entry(title)
    
    if doc == None:
        # Si el documento no existe, mostrar página de error
        return render(request, "encyclopedia/error.html", {"title": title}) 
    
    # Si el documento existe, convertirlo a HTML
    doc_html = markdown.markdown(doc)

    return render(request, "encyclopedia/entrada.html", {"doc": doc_html, "title": title})
