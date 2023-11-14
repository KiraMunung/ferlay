
#from .forms import UserForm, ProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
import docx



# Create your views here.
def acceuil(request):
    return render(request, 'tfc/espace.html')

def option(request):
    return render(request, 'tfc/option.html')

def espace(request):
    return render(request, 'tfc/espace.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('option')
            else:
                messages.error(request, "L'utilisateur est désactivé.")
        else:
            messages.error(request, "Le nom d'utilisateur ou le mot de passe est incorrect.")
    return render(request, 'tfc/login.html')




def create_word(request):
    if request.method == 'POST':
        # Récupérer le contenu du formulaire
        content = request.POST.get('content')

        # Créer un nouveau document Word
        document = docx.Document()

        # Ajouter le contenu au document
        document.add_paragraph(content)

        # Enregistrer le document Word
        document.save('created_word.docx')

        # Télécharger le fichier Word créé
        with open('created_word.docx', 'rb') as f:
            response = HttpResponse(f.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename="created_word.docx"'
            return response

    return render(request, 'tfc/create_word.html')


from django.shortcuts import render



from reportlab.pdfgen import canvas
from io import BytesIO

import webbrowser
from PyPDF2 import PdfReader, PdfWriter
from django.http import HttpResponse

def scan_and_modify_pdf(request):
    if request.method == 'POST' and request.FILES['pdf']:
        pdf_file = request.FILES['pdf']

        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        pdf_writer = PdfWriter()

        # Parcourir les pages du document PDF
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            # Effectuer les modifications nécessaires sur la page
            # ...

            pdf_writer.add_page(page)

        # Enregistrer le document PDF modifié
        output_pdf_path = 'modified_pdf.pdf'
        output_pdf = open(output_pdf_path, 'wb')
        pdf_writer.write(output_pdf)
        output_pdf.close()

        # Ouvrir le fichier PDF avec le navigateur par défaut
        webbrowser.open(output_pdf_path)

        return HttpResponse("PDF modifié et ouvert avec succès.")

    return render(request, 'tfc/scan_and_modify_pdf.html')




from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import os

def share_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)

        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return redirect('share_file_email', file_name=file.name)

    return render(request, 'tfc/share.html')





from django.core.mail import EmailMessage

def share_file_email(request, file_name):
    if request.method == 'POST':
        sender_email = 'votre_email@gmail.com'
        sender_password = 'votre_mot_de_passe'
        receiver_email = request.POST.get('receiver_email')

        file_path = os.path.join(settings.MEDIA_ROOT, file_name)

        # Créer un objet EmailMessage
        message = EmailMessage()
        message['Subject'] = 'Partage de fichier'
        message['From'] = sender_email
        message['To'] = receiver_email

        # Lire le fichier en pièce jointe
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Ajouter le fichier en pièce jointe
        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        # Envoyer l'email via SMTP
        message.send()

        return render(request, 'tfc/email_success.html')

    return render(request, 'tfc/email_form.html')




from django.shortcuts import render
from .models import Etudiant, Dossier, Fichier

def recherche_dossier(request):
    if request.method == 'POST':
        matricule = request.POST.get('matricule')
        etudiant = Etudiant.objects.get(matricule=matricule)
        dossiers = Dossier.objects.filter(etudiant=etudiant)
        return render(request, 'tfc/recherche_dossier.html', {'dossiers': dossiers})
    return render(request, 'tfc/recherche_dossier.html')

def afficher_fichiers_dossier(request, dossier_id):
    dossier = Dossier.objects.get(id=dossier_id)
    fichiers = Fichier.objects.filter(dossier=dossier)
    return render(request, 'tfc/afficher_fichiers_dossier.html', {'dossier': dossier, 'fichiers': fichiers})


from .forms import EtudianForm
def enregistrer(request):
    if request.method == 'POST':
        form = EtudianForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/information/')
            return render(request, 'tfc/option.html')
    else:
        form = EtudianForm()
    return render(request, 'tfc/ceeretudiant.html', {'form': form})