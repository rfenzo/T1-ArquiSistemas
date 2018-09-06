from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
    'class':'textarea',
    'placeholder':'Add a new comment!',
    'rows':2}
    ))

