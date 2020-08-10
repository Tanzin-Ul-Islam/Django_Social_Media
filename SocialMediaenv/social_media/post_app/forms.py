from django import forms
from post_app.models import *

class newpost(forms.ModelForm):
    class Meta:
        model = post
        fields=['image', 'caption']