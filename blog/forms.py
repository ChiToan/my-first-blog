from django import forms
from .models import Post, Profile

class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'size':80}))
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Post
        fields = ('title', 'text',)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio',)