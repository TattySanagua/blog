from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post #El modelo es Post
        fields = ('title', 'text') #Campos que deben exponerse en el formulario

