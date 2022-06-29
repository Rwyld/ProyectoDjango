from django import forms

class Registro(forms.Form):
    user = forms.CharField()
    email = forms.CharField()
    contraseña = forms.CharField()
