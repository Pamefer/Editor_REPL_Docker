from django.forms import Form, ModelForm, PasswordInput, CharField
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms

from . import models as mod

#1
class CodigoForm(ModelForm):
    class Meta:
        model = mod.Codigo
        fields = '__all__'
#         #exclude = ('iduser',)
#         # widgets = {x`x`
#         #           'enlace': forms.TextInput(attrs={'class': 'form-control fields-pl', 'placeholder': 'enlace'}),
#         #           'codigodes':forms.TextInput(attrs={'class': 'form-control fields-pl', 'placeholder': 'codigo'}),
#         #           'iduser': forms.HiddenInput(),}


#2
# class CodigoForm(Form):
#     id_usuario_id = forms.CharField(label='',widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'id'}))
#     enlace = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enlace'}))
#     codigodes = forms.CharField(label='',min_length=5,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'codigo'}))
#
#     def clean(self):
#         clean_data = super(CodigoForm, self).clean()
#
#     def save(self, commit=True):
#         data_orig = self.cleaned_data
#         data = {}
#         u=mod.Codigo(**data)
#
#         u.save()


#3
# class CodigoForm(ModelForm):
#     class Meta:
#         model = mod.Codigo
#         #fields = ['enlace', 'codigodes','id_usuario']
#         fields = '__all__'
#         widgets = {
#                   'enlace': forms.TextInput(attrs={'class': 'form-control fields-pl', 'placeholder': 'enlace'}),
#                   'codigodes':forms.TextInput(attrs={'class': 'form-control fields-pl', 'placeholder': 'codigo'}),
#                    'id_usuario': forms.HiddenInput(),
#         }


class FormLogin(Form):
    username = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre de usuario'}))
    password = forms.CharField(label='', required=True,  widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Contrasenia'}))
    def clean(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            invalido = ValidationError(
                ('Nombre de usuario o clave invalidos'),
            )
        print("holaaaaaaaaaaaaaa",user)

        if user is None:
            print('usernameeeeeeee')
            # raise forms.ValidationError('Nombre de usuario o clave invalidos')
            self.add_error('password', invalido)

#Valeeeeeeeeeeeeeeeeeeee
# class CodigoForm(forms.Form):
#     id_usuario = forms.CharField(max_length=100)
#     enlace = forms.CharField(widget=forms.Textarea)
#     codigodes = forms.CharField(widget=forms.Textarea)
#     def clean(self):
#         return self.cleaned_data
