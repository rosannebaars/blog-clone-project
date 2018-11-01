from django import forms
from blog.models import Post, Comment

# To style a particular widhet we cann add a widgets attribute to the meta class
# A widget attribute actually a dictionary in which you pass in some arguments that
# link the actual widget to the class. Later you can call in your CSS file the
# class name and it will affect that particular widget directly

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            # Textinputclass is our own class
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
            # We are connecting to three CSS classes:
                # editable(means we can't edit it)
                # medium-editor-textarea (gives the styling)
                # postcontent (our own class)
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
