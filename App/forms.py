from django import forms
 
class CategoriaFormulario(forms.Form):
    nombre = forms.CharField()

class BuscarCategoria(forms.Form):
    nombre = forms.CharField()

class SubcategoriaFormulario(forms.Form):
    nombre = forms.CharField()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    color = forms.CharField()
    talle = forms.CharField()