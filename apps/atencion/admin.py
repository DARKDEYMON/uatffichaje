from django.contrib import admin
from .models import *

# Register your models here.
class FichasAdmin(admin.ModelAdmin):
    list_display = ('id', 'ci', 'nombre_apellidos','fecha','atendido')
    search_fields = ['id', 'ci', 'nombre_apellidos','fecha','atendido']
admin.site.register(fichas,FichasAdmin)