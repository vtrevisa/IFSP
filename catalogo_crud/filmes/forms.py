from .models import Filme
from django import forms
class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = [
            "titulo", "tipo", "genero",
            "ano", "assistido", "nota"
        ]

    def clean_nota(self):
        nota = self.cleaned_data.get("nota")
        if nota is not None and not 1 <= nota <= 5:
            raise forms.ValidationError(
                "A nota deve estar entre 1 e 5."
            )
        return nota
