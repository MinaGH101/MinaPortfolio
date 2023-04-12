from django import forms
from .models import Messages



class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'message')