from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm
from django.db.models import Q
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def categoria_form(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_form.html', {'form': form})

def producto_form(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

def cliente_form(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})


# myapp/views.py
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm, BusquedaForm

def buscar(request):
    resultados_categoria = []
    resultados_producto = []
    resultados_cliente = []

    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query', '')  # Usar get para manejar el caso en el que 'query' no está presente
            resultados_categoria = Categoria.objects.filter(nombre__icontains=query)
            resultados_producto = Producto.objects.filter(Q(nombre__icontains=query) | Q(categoria__nombre__icontains=query))
            resultados_cliente = Cliente.objects.filter(Q(nombre__icontains=query) | Q(correo__icontains=query))
    else:
        form = BusquedaForm()

    return render(request, 'busqueda_resultados.html', {
        'form': form,
        'resultados_categoria': resultados_categoria,
        'resultados_producto': resultados_producto,
        'resultados_cliente': resultados_cliente,
    })