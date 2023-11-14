from django.contrib import admin
from .models import Etudiant, Dossier, Fichier
# Register your models here.


class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'post_nom', 'prenom', 'promotion', 'filiere', 'adresse')
    search_fields = ['matricule']


class DossierAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom']

class FichierAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom']

admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Dossier, DossierAdmin)
admin.site.register(Fichier, FichierAdmin)