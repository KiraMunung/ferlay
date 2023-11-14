from django.db import models

# Create your models here.

dossier = (
    ('B', 'Panda'),
    ('Shituru', 'Shituru'),
    ('Likasi', 'Likasi'),
    ('Kikula', 'Kikula')
)

class Etudiant(models.Model):
    matricule = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    post_nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    promotion = models.CharField(max_length=30)
    filiere = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Dossier(models.Model):
    nom = models.CharField(max_length=30)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Fichier(models.Model):
    nom =models.CharField(max_length=30)
    fichier = models.FileField(upload_to="fichier")
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)