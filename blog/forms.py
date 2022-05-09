from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:  # helper class 
        model = Post
        fields = ['title', 'text'] #  once again we will create a link to the forms page, a URL, a view and a template

# this will be my search box 
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)