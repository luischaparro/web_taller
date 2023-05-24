from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "GET":
        dato = get_object_or_404(Tipodocumento, id=dato_id)
        form = TipodocumentoForm(instance=dato)
        return render(request, "dato_modificar.html", {
            "dato": dato,
            "form": form,
            "tipo": "Documento"
        })
    else:
        try:
            dato = get_object_or_404(Tipodocumento, id=dato_id)
            form = TipodocumentoForm(request.POST ,instance=dato)
            form.save()
            return redirect("datos")
        except:
            return render(request, "dato_modificar.html", {
                "dato": dato,
                "form": form,
                "tipo": "Documento",
                "error": "Algo salio mal"
            })

def datos_ver_C(request, dato_id):
    if request.method == "GET":
        dato = get_object_or_404(Ciudad, id=dato_id)
        form = CiudadForm(instance=dato)
        return render(request, "dato_modificar.html", {
            "dato": dato,
            "form": form,
            "tipo": "Ciudad"
        })
    else:
        try:
            dato = get_object_or_404(Ciudad, id=dato_id)
            form = CiudadForm(request.POST ,instance=dato)
            form.save()
            return redirect("datos")
        except:
            return render(request, "dato_modificar.html", {
                "dato": dato,
                "form": form,
                "tipo": "Ciudad",
                "error": "Algo salio mal"
            })

def datos_ver_P(request, dato_id):
    if request.method == "GET":
        dato = get_object_or_404(Persona, id=dato_id)
        form = PersonaForm(instance=dato)
        return render(request, "dato_modificar.html", {
            "dato": dato,
            "form": form,
            "tipo": "Persona"
        })
    else:
        try:
            dato = get_object_or_404(Persona, id=dato_id)
            form = PersonaForm(request.POST ,instance=dato)
            form.save()
            return redirect("datos")
        except:
            return render(request, "dato_modificar.html", {
                "dato": dato,
                "form": form,
                "tipo": "Persona",
                "error": "Algo salio mal"
            })

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
                "name": "Documento",
                "error": "error"
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
                "name": "Ciudad",
                "error": "error"
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
                "name": "Persona",
                "error": "error"
            })

def datos_ver_delete(request,dato_id, tipo):
    if request.method == "GET":
        if tipo == "Documento":
            dato = get_object_or_404(Tipodocumento, id=dato_id)
            dato.delete()
            return redirect("datos")
        elif tipo == "Ciudad":
            dato = get_object_or_404(Ciudad, id=dato_id)
            dato.delete()
            return redirect("datos")
        elif tipo == "Persona":
            dato = get_object_or_404(Persona, id=dato_id)
            dato.delete()
            return redirect("datos")
        





