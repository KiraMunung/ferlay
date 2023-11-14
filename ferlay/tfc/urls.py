from django.urls import path
from .views import acceuil, user_login, espace, create_word, scan_and_modify_pdf, share_file, share_file_email, recherche_dossier,afficher_fichiers_dossier,option,enregistrer
from django.contrib.auth import views
#app_name = 'utilisateurs'
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', acceuil, name="acceuil"),
    #path('register', register, name="register"),
    path('login', user_login, name="login"),
    #path('logout', user_logout, name="logout"),
    path('espace', espace, name="espace"),
    path('word', create_word, name="create_word"),
    path('scan', scan_and_modify_pdf, name="scan_and_modify_pdf"),
    path('share', share_file, name="share"),
    #path('mail', share_file_email, name="email_form"),
    path('share/email/<str:file_name>/', share_file_email, name='share_file_email'),
    path('recherche', recherche_dossier, name="recherche_dossier"),
    path('dossier/<int:dossier_id>/', afficher_fichiers_dossier, name='afficher_fichiers_dossier'),
    path('option', option, name="option"),
    path('etudiant', enregistrer, name="ceeretudiant"),
]