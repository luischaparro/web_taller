from django.forms import ModelForm
from .models import Tipodocumento, Persona, Ciudad

class TipodocumentoForm(ModelForm):
    class Meta:
        model = Tipodocumento
        fields = ["nombre", "descripcion"]

class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = ["nombre", "descripcion"]

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ["nombres", "apellidos", "idtipodocumento", "documento", "lugarresidencia", "fechanacimiento", 
                  "email", "telefono", "usuario", "password"]