from django.contrib import admin

# Register your models here.
from .models import Artiste, Chanson

class ArtisteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'style']

admin.site.register(Artiste, ArtisteAdmin)

class ChansonAdmin(admin.ModelAdmin):
    list_display = ['id', 'titre', 'durée', "artiste"]

admin.site.register(Chanson, ChansonAdmin)