from django.forms import forms
from .models import Event,Committee,Blogs

class eventform(froms.ModelForm):
    class meta:
        model=Event
        fields=["title","event_date","images","description"]

class blogform(forms.ModelForm):
    class meta:
        model=Blogs
        files=["title","subtitle","description","image"]