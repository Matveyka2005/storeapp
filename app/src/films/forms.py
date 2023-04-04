from django import forms
from .models import Film


class FilmForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
    class Meta:
        model = Film 
        fields = ('name', 'about', 'image', 'video', 'author', 'category')
