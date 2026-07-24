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
            return render(request, 'contact/thanks.html', {'name': form.cleaned_data['nom_complet']})
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})
