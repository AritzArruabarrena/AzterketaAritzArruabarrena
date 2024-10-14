from django import forms
from .models import *


class PazienteForm(forms.ModelForm):
    class Meta:
        model=Paziente
        fields=['id','izena','abizena','jaiotze_data']
        

class MedikoForm(forms.ModelForm):
    class Meta:
        model=Medikua
        fields=['id','izena','abizena','jaiotze_data']
        

class ZitakForm(forms.ModelForm):
    class Meta:
        model=Zitak
        fields=['hasiera_data','bukaera_data','mediku_id','paziente_id']
        

class PazienteEditatuForm(forms.ModelForm):
    class Meta:
        model=Paziente
        fields=['id','izena','abizena','jaiotze_data']
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].disabled =True
        

class MedikuaEditatuForm(forms.ModelForm):
    class Meta:
        model=Medikua
        fields=['id','izena','abizena','jaiotze_data']
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].disabled =True