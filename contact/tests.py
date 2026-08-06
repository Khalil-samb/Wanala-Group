from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class ContactViewTests(TestCase):
    def test_contact_form_saves_message_and_shows_success(self):
        response = self.client.post(
            reverse('contact:contact'),
            {
                'nom_complet': 'Jean Dupont',
                'email': 'jean@example.com',
                'telephone': '+221776543210',
                'adresse': 'Dakar',
                'besoin': 'Besoin d’un devis pour un projet.',
                'pole_concerne': 'Mobility',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')
        self.assertContains(response, 'Votre demande a bien été envoyée')
        self.assertTrue(ContactMessage.objects.filter(nom_complet='Jean Dupont').exists())

    def test_contact_form_exposes_poles_as_choices(self):
        form = self.client.get(reverse('contact:contact')).context['form']
        self.assertIn(('Mobility', 'Mobility'), form.fields['pole_concerne'].choices)
        self.assertIn(('Solutions', 'Solutions'), form.fields['pole_concerne'].choices)
