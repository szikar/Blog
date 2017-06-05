from    django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title',) 'text',)

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=SummernoteWidget())

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
