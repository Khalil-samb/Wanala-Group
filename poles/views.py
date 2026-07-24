from django.shortcuts import render, get_object_or_404, redirect
from .models import Pole
import urllib.parse


DEFAULT_POLES = [
    ('mobility', 'Mobility', 'Des solutions de mobilité complètes pour accompagner vos déplacements, vos opérations et vos projets de développement.'),
    ('solutions', 'Solutions', 'Des solutions adaptées aux entreprises et particuliers pour répondre à des besoins concrets et performants.'),
    ('immobilier', 'Immobilier', 'Gestion locative, location meublée et transactions immobilières avec un accompagnement de bout en bout.'),
    ('invest', 'Invest', 'Des investissements stratégiques et une gestion financière solide pour construire votre avenir.'),
    ('international', 'International', 'Une ouverture internationale et un accompagnement sur mesure pour vos projets au-delà des frontières.'),
]


def ensure_default_poles():
    for slug, name, description in DEFAULT_POLES:
        Pole.objects.get_or_create(slug=slug, defaults={'name': name, 'description': description})


def list_poles(request):
    ensure_default_poles()
    poles = Pole.objects.all().order_by('name')
    return render(request, 'poles/list.html', {'poles': poles})


def detail(request, slug):
    ensure_default_poles()
    pole = get_object_or_404(Pole, slug=slug)
    template_name = f'poles/{slug}.html' if slug in {'mobility', 'solutions', 'immobilier', 'invest', 'international'} else 'poles/detail.html'
    return render(request, template_name, {'pole': pole, 'poles': Pole.objects.all().order_by('name')})


def request_service(request, slug):
    pole = get_object_or_404(Pole, slug=slug)
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        # Use provided number (assume country code +221 for Senegal)
        number = '+221773907069'
        text = f"Demande de service pour le pôle {pole.name}.\nNom: {name}\nEmail: {email}\nMessage: {message}"
        wa_url = f"https://wa.me/{number}?text={urllib.parse.quote_plus(text)}"
        return redirect(wa_url)
    return redirect('poles:detail', slug=slug)
