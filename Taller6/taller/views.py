from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from .forms import TipodocumentoForm, CiudadForm, PersonaForm
from .models import Tipodocumento, Persona, Ciudad

# Create your views here.
def home(request):
    return render(request, "home.html")

def datos(request):
    objetosD = Tipodocumento.objects.all()
    objetosC = Ciudad.objects.all()
    objetosP = Persona.objects.all()
    return render(request, "datos.html", {
        "objetosD": objetosD,
        "objetosC": objetosC,
        "objetosP": objetosP
    })

def datos_ver_D(request, dato_id):
    dato = get_list_or_404(Tipodocumento, pk=dato_id)
    form = TipodocumentoForm(instance=dato)
    return render(request, "dato_modificar.html", {
        "task": dato,
        "form": form
    })

def datos_ver_C(request, dato_id):

    return render(request, "")

def datos_ver_P(request, dato_id):

    return render(request, "")

def datos_crear(request):
    return render(request, "datos_crear.html", {
        "form1": TipodocumentoForm,
        "form2": CiudadForm,
        "form3": PersonaForm
    })

def datos_crear_documento(request):
    if request.method == "GET":
        return render(request, "forms.html", {
            "form": TipodocumentoForm,
            "name": "Documento"
        })
    else:
        try:
            form = TipodocumentoForm(request.POST)
            new_dato = form.save(commit=False)
            new_dato.save()
            return redirect("datos")
        except:
            return render(request, "forms.html", {
                "form": TipodocumentoForm,
                "name": "Documento"
            })
    

def datos_crear_ciudad(request):
    if request.method == "GET":
        return render(request, "forms.html", {
            "form": CiudadForm,
            "name": "Ciudad"
        })
    else:
        try:
            form = CiudadForm(request.POST)
            new_dato = form.save(commit=False)
            new_dato.save()
            return redirect("datos")
        except:
            return render(request, "forms.html", {
                "form": CiudadForm,
                "name": "Ciudad"
            })


def datos_crear_persona(request):
    if request.method == "GET":
        return render(request, "forms.html", {
            "form": PersonaForm,
            "name": "Persona"
        })
    else:
        try:
            form = PersonaForm(request.POST)
            new_dato = form.save(commit=False)
            new_dato.save()
            return redirect("datos")
        except:
            return render(request, "forms.html", {
                "form": PersonaForm,
                "name": "Persona"
            })




