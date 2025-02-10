from django import forms
from .models import Event,Committee,Blogs,CommitteeMember,Notice,mission_vision,AddDonor,EventImage
from django.contrib.auth.models import User

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=["username","password"]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_date', 'description']

    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}), required=False)

    
class EventImageForm(forms.ModelForm):
    class Meta:
        model = EventImage
        fields = ['image']
        

class blogform(forms.ModelForm):
    class Meta:
        models=Blogs
        fields="__all__"
        
class committeeform(forms.ModelForm):
    class Meta:
        model= Committee
        fields=['name','start_date','end_date','is_current']
        
        

        
class memberform(forms.ModelForm):
    c_id = forms.ModelChoiceField(
        queryset=Committee.objects.all(),
        empty_label="Select Committee",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model=CommitteeMember
        fields=['name', 'address', 'position', 'image', 'c_id', 'user']