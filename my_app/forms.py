from django import forms
from .models import *

class ServerForm(forms.ModelForm):

    class Meta:
        model = ServerImages
        fields = '__all__'