from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Введите заголовок", 'class': 'my-form'}),
            'content': forms.Textarea(attrs={'placeholder': "Введите контент", 'rows': 5, 'class': 'my-form'})
        }