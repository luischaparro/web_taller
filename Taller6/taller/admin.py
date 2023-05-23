from django.contrib import admin
from .models import Tipodocumento, Ciudad, Persona

# Register your models here.
admin.site.register(Tipodocumento)
admin.site.register(Ciudad)
admin.site.register(Persona)