from django.forms import ModelForm
from .models import Etudiant

class EtudianForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ['matricule', 'nom', 'post_nom', 'prenom', 'promotion', 'filiere']