from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm
from .models import ContactMessage


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                nom_complet=form.cleaned_data['nom_complet'],
                email=form.cleaned_data['email'],
                telephone=form.cleaned_data.get('telephone', ''),
                adresse=form.cleaned_data.get('adresse', ''),
                besoin=form.cleaned_data['besoin'],
                pole_concerne=form.cleaned_data.get('pole_concerne', ''),
            )

            full_name = form.cleaned_data['nom_complet']
            email = form.cleaned_data['email']
            pole = form.cleaned_data.get('pole_concerne', 'Non précisé')
            subject = f"Nouvelle demande de contact - {full_name}"
            body = (
                f"Nom complet : {full_name}\n"
                f"Email : {email}\n"
                f"Téléphone : {form.cleaned_data.get('telephone', '') or 'Non renseigné'}\n"
                f"Adresse : {form.cleaned_data.get('adresse', '') or 'Non renseignée'}\n"
                f"Pôle concerné : {pole}\n\n"
                f"Besoin :\n{form.cleaned_data['besoin']}"
            )

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except Exception:
                messages.error(request, 'Votre demande a bien été enregistrée, mais l’email de notification n’a pas pu être envoyé.')
            else:
                messages.success(request, 'Votre demande a bien été envoyée. Nous vous recontacterons très prochainement.')

            return render(request, 'contact/contact_form.html', {'form': ContactForm()})

        messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
        return render(request, 'contact/contact_form.html', {'form': form})

    form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})
