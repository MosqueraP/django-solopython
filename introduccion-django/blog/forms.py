from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        # Campos del formulario a partir de la bd
        fields=('title', 'content')