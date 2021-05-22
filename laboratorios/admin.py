from django.contrib import admin

# Register your models here.
from .models import Laboratorio,Registro,Usuario

admin.site.register(Laboratorio)
admin.site.register(Registro)
admin.site.register(Usuario)



