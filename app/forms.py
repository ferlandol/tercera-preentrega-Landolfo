from django import forms
from .models import Categoria, Producto, Cliente

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo']


class BusquedaForm(forms.Form):
    query = forms.CharField(label='Buscar')