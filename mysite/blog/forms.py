from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields that we want to user to edit
        fields = ('author','title', 'text',)
        # widgets to add css styling here postcontent and textinputclass are for custom styling rest are predefined
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
