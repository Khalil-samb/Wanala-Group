from django import forms


POLE_CHOICES = [
    ('', 'Sélectionnez un pôle'),
    ('Mobility', 'Mobility'),
    ('Solutions', 'Solutions'),
    ('Immobilier', 'Immobilier'),
    ('Invest', 'Invest'),
    ('International', 'International'),
]


class ContactForm(forms.Form):
    nom_complet = forms.CharField(max_length=255, label='Nom complet')
    email = forms.EmailField(label='Email professionnel')
    telephone = forms.CharField(max_length=50, required=False, label='Numéro Téléphone')
    adresse = forms.CharField(max_length=255, required=False, label='Adresse Postal')
    besoin = forms.CharField(widget=forms.Textarea, label='Décrivez votre besoin')
    pole_concerne = forms.ChoiceField(choices=POLE_CHOICES, required=False, label='Pôle concerné')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_class = 'w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-800 outline-none transition focus:border-amber-500 focus:ring-4 focus:ring-amber-100'
        textarea_class = 'w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-800 outline-none transition focus:border-amber-500 focus:ring-4 focus:ring-amber-100 min-h-[140px] resize-y'

        self.fields['nom_complet'].widget.attrs.update({'class': input_class, 'placeholder': 'Votre nom complet'})
        self.fields['email'].widget.attrs.update({'class': input_class, 'placeholder': 'vous@email.com'})
        self.fields['telephone'].widget.attrs.update({'class': input_class, 'placeholder': '+221 77 000 00 00'})
        self.fields['adresse'].widget.attrs.update({'class': input_class, 'placeholder': 'Votre adresse'})
        self.fields['besoin'].widget.attrs.update({'class': textarea_class, 'placeholder': 'Expliquez-nous votre besoin'})
        self.fields['pole_concerne'].widget.attrs.update({'class': input_class})

    def clean_nom_complet(self):
        nom = self.cleaned_data.get('nom_complet', '')
        return nom.strip()

    def clean_besoin(self):
        besoin = self.cleaned_data.get('besoin', '')
        return besoin.strip()
