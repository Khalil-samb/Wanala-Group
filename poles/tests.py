from django.test import TestCase
from django.urls import reverse

from .models import Pole


class PolePagesTests(TestCase):
    def test_default_poles_are_available(self):
        expected_slugs = ['mobility', 'solutions', 'immobilier', 'invest', 'international']

        self.assertEqual(Pole.objects.filter(slug__in=expected_slugs).count(), 5)

        for slug in expected_slugs:
            response = self.client.get(reverse('poles:detail', kwargs={'slug': slug}))
            self.assertEqual(response.status_code, 200)

    def test_homepage_displays_pole_links_in_header(self):
        response = self.client.get(reverse('core:home'))
        self.assertContains(response, 'Mobility')
        self.assertContains(response, 'Solutions')
        self.assertContains(response, 'Immobilier')
        self.assertContains(response, 'Invest')
        self.assertContains(response, 'International')
