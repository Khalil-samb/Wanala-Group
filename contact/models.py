from django.db import models


class ContactMessage(models.Model):
    nom_complet = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=50, blank=True)
    adresse = models.CharField(max_length=255, blank=True)
    besoin = models.TextField()
    pole_concerne = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Message de contact'
        verbose_name_plural = 'Messages de contact'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nom_complet} - {self.email}"
