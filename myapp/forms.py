from cProfile import label
from ftplib import MAXLINE
from django import forms
#from .models import CustomUser
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico')
    full_name = forms.CharField(max_length=255, label='Nombre Completo')

    class Meta:
        model = CustomUser
        fields = ['email', 'full_name', 'password1', 'password2']

class RecomendacionForm(forms.Form):
    MARCA_CHOICES = [
        ('The ordinary', 'The ordinary'),
        ('CERAVE', 'CERAVE'),
        ('eucerin', 'Eucerin'),
        ('La Roche-Posay', 'La Roche-Posay'),
        ('Clinique', 'Clinique'),
        ('Garnier', 'Garnier'),
        ('Bioderma', 'Bioderma'),
        ('Cetaphil', 'Cetaphil')
        
    ]

    TIPO_PIEL_CHOICES = [
        ('Normal', 'Normal'),
        ('Grasa', 'Grasa'),
        ('Seca', 'Seca'),
        ('Mixta', 'Mixta'),
        ('Sensible', 'Sensible'),
        ('Todo tipo de piel', 'Todo tipo de piel'),
        ('Normal a seca', 'Normal a seca'),
        ('Normal a grasa', 'Normal a grasa')
    ]

    PROBLEMAS_PIEL_CHOICES = [
        ('acné', 'Acné'),
        ('manchas', 'Manchas'),
        ('arrugas', 'Arrugas'),
        ('deshidratación', 'Deshidratación'),
        ('ojeras', 'Ojeras'),
        ('limpieza', 'Limpieza'),
        ('vejez', 'Vejez'),
        ('irritación', 'Irritación'),
        ('piel opaca', 'Piel opaca'),
        ('puntos negros', 'Puntos negros'),
        ('piel agrietada', 'Piel agrietada'),
        ('rosácea', 'Rosácea'),
        ('poros', 'Poros'),
        ('brotes', 'Brotes'),
        ('hiperpigmentación', 'Hiperpigmentación'),
        ('tono desigual de la piel', 'Tono desigual de la piel')

    ]
    marca = forms.ChoiceField(choices=MARCA_CHOICES, label='Marca')
    tipo_de_piel = forms.ChoiceField(choices=TIPO_PIEL_CHOICES, label='Tipo de Piel')
    problemas_piel = forms.MultipleChoiceField(
        choices=PROBLEMAS_PIEL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Problemas de Piel',
        required=False
    )

#class CreateNewTask(forms.Form):
  #  title = forms.CharField(label="Titulo de tarea", max_length=200)
   # description=forms.CharField(widget=forms.Textarea) 