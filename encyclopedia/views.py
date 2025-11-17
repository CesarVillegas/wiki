from django.shortcuts import render
import markdown
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
from .forms import NuevoSearchForm, NuevaEntradaForm


# Vista para la página de índice que lista todas las entradas de la enciclopedia
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NuevoSearchForm()
    })


# Vista para mostrar una entrada específica de la enciclopedia
def entrada(request, title):
    doc = util.get_entry(title)
    
    if doc == None:
        # Si el documento no existe, mostrar página de error
        return render(request, "encyclopedia/error.html", {"title": title}) 
    
    # Si el documento existe, convertirlo a HTML
    doc_html = markdown.markdown(doc)

    return render(request, "encyclopedia/entrada.html", {
        "doc": doc_html,
        "title": title, 
        "form": NuevoSearchForm()
    })


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
            "entradas": entradas_encontradas,
            "form": NuevoSearchForm()
        })
    
    # Si no es un POST, redirigir al índice
    return render(request, "encyclopedia/index.html", {
            "form": NuevoSearchForm(),
            "entries": util.list_entries()
    })


# Vista para crear una nueva entrada en la enciclopedia
def crear_entrada(request):

    if request.method == "POST":
        formEntrada = NuevaEntradaForm(request.POST)
        if formEntrada.is_valid():
            title = formEntrada.cleaned_data["title"]
            content = formEntrada.cleaned_data["content"]
            if util.save_entry(title, content):
                # Se guardo exitosamente la nueva entrada
                return HttpResponseRedirect(reverse("encyclopedia:entrada", args=[title]))
            else :
                return render(request, "encyclopedia/crear_entrada.html", {
                    "error": "An entry with this title already exists.",
                    "entries": util.list_entries(),
                    "form": NuevoSearchForm(),
                    "formEntrada":  formEntrada
                })
        else:  # Form is not valid
            return render(request, "encyclopedia/crear_entrada.html", {
                "entries": util.list_entries(),
                "formEntrada":  formEntrada,
                "form": NuevoSearchForm()
            })
    else:
        return render(request, "encyclopedia/crear_entrada.html", {
            "entries": util.list_entries(),
            "formEntrada":  NuevaEntradaForm(),
            "form": NuevoSearchForm()
        })