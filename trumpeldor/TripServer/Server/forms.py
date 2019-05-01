# forms.py
from django import forms
from .models import *


class ImagesForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = ['name', 'img']


class VideosForm(forms.ModelForm):

    class Meta:
        model = Videos
        fields = ['name', 'vid']
