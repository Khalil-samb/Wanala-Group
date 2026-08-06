from django.shortcuts import render

WHATSAPP_NUMBER = "221773907069"
WHATSAPP_BASE_URL = f"https://wa.me/{WHATSAPP_NUMBER}?text="


def _build_whatsapp_link(message: str) -> str:
    return f"{WHATSAPP_BASE_URL}{message}"


def _render_pole_page(request, template_name, message):
    return render(
        request,
        template_name,
        {
            "whatsapp_number": WHATSAPP_NUMBER,
            "whatsapp_link": _build_whatsapp_link(message),
        },
    )


def immobilier(request):
    return _render_pole_page(
        request,
        'poles/immobilier.html',
        "Bonjour%20WANALA%20Immobilier%2C%20je%20souhaite%20obtenir%20un%20accompagnement%20pour%20la%20gestion%20ou%20la%20valorisation%20de%20mon%20bien.",
    )


def invest(request):
    return _render_pole_page(
        request,
        'poles/invest.html',
        "Bonjour%20WANALA%20Invest%2C%20je%20souhaite%20discuter%20de%20mes%20objectifs%20d'investissement%20et%20b%C3%A9n%C3%A9ficier%20de%20vos%20conseils%20sur%20mesure.",
    )


def international(request):
    return _render_pole_page(
        request,
        'poles/international.html',
        "Bonjour%20WANALA%20International%2C%20je%20souhaite%20discuter%20d'un%20projet%20d'import%2Fexport%20ou%20d'expansion%20internationale.",
    )


def mobility(request):
    return _render_pole_page(
        request,
        'poles/mobility.html',
        "Bonjour%20WANALA%20Mobility%2C%20je%20souhaite%20obtenir%20plus%20d'informations%20sur%20vos%20solutions%20de%20mobilit%C3%A9%20pour%20mon%20projet.",
    )


def solutions(request):
    return _render_pole_page(
        request,
        'poles/solutions.html',
        "Bonjour%20WANALA%20Solutions%2C%20je%20souhaite%20obtenir%20un%20devis%20pour%20les%20services%20de%20nettoyage%20et%20d'hygi%C3%A8ne%20adapt%C3%A9s%20%C3%A0%20mes%20besoins.",
    )
