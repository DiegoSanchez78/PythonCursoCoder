from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=25)
    camada = forms.IntegerField()

class BuscarForm(forms.Form):
    nombre = forms.CharField(max_length=25)

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
    telefono = forms.IntegerField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField()
    telefono = forms.IntegerField()