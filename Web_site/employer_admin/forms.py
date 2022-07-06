from survey.models import EmployerAdminAuth
from django.forms import ModelForm, TextInput,PasswordInput,CheckboxInput,Textarea,FileInput
from django import forms
class EAdminAuthForm(ModelForm):
    class Meta:
        model = EmployerAdminAuth
        fields = ["login","password_e"]
        exclude = ["identifier"]
        widgets = {
            "login": TextInput(attrs={
                "class": "name",
                "placeholder": "Login",
                "type": "text"
            }),
            "password_e": PasswordInput(render_value=True,attrs={
                "class": "password",
                "placeholder": "Password",
                "type": "password"
            })
        }
