from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class ContactViewTests(TestCase):
    def test_contact_form_saves_message(self):
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
        self.assertTemplateUsed(response, 'contact/thanks.html')
        self.assertTrue(ContactMessage.objects.filter(nom_complet='Jean Dupont').exists())
