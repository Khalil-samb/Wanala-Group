from django import forms


class ContactForm(forms.Form):
    nom_complet = forms.CharField(max_length=255, label='Nom complet')
    email = forms.EmailField(label='Email professionnel')
    telephone = forms.CharField(max_length=50, required=False, label='Numéro Téléphone')
    adresse = forms.CharField(max_length=255, required=False, label='Adresse Postal')
    besoin = forms.CharField(widget=forms.Textarea, label='Décrivez votre besoin')
    pole_concerne = forms.CharField(max_length=100, required=False, label='Pôle concerné')

    def clean_nom_complet(self):
        nom = self.cleaned_data.get('nom_complet', '')
        return nom.strip()

    def clean_besoin(self):
        besoin = self.cleaned_data.get('besoin', '')
        return besoin.strip()
