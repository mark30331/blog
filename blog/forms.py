from django import forms
from .models import Comment_Table

class CommentForm(forms.ModelForm): # create a form from the model --> comment_table
    class Meta:
        model = Comment_Table
        fields = ['name','email', 'body'] # to specify which model attribute to include in the form. 