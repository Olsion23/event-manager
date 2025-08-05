from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'descriptions', 'date', 'time', 'location']
        widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
        'descriptions': forms.Textarea(attrs={'class':'form-control'}),
        'date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        'time': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
        'location': forms.TextInput(attrs={'class':'form-control'})

        }
