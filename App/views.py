from django.shortcuts import render
from App.forms import CategoriaFormulario, BuscarCategoria, SubcategoriaFormulario, ProductoFormulario
from App.models import Categoria, Subcategoria, Producto

# Create your views here.
def inicio(request):
    return render(request, "App/inicio.html")
def about(request):
    return render(request, "App/about.html")
def projects(request):
    return render(request, "App/projects.html")
def signup(request):
    return render(request, "App/signup.html")

# Cargar categorias

def cargar_categoria(request):
 
      if request.method == "POST":
 
            miFormulario = CategoriaFormulario(request.POST) # Aqui me llega la informacion del html
            #print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data

                  categoria = Categoria(nombre=informacion["nombre"])
                  categoria.save()
                  return render(request, "App/about.html")
      else:
            miFormulario = CategoriaFormulario()
 
      return render(request, "App/cargar_categoria.html", {"miFormulario": miFormulario})

# Cargar subcategorias

def cargar_subcategoria(request):
 
      if request.method == "POST":
 
            miFormulario = SubcategoriaFormulario(request.POST) # Aqui me llega la informacion del html
            #print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data

                  subcategoria = Subcategoria(nombre=informacion["nombre"])
                  subcategoria.save()
                  return render(request, "App/about.html")
      else:
            miFormulario = SubcategoriaFormulario()
 
      return render(request, "App/cargar_subcategoria.html", {"miFormulario": miFormulario})

# Cargar productos

def cargar_producto(request):
 
      if request.method == "POST":
 
            miFormulario = ProductoFormulario(request.POST) # Aqui me llega la informacion del html
            #print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data

                  producto = Producto(nombre=informacion["nombre"], color=informacion["color"], talle=informacion["talle"] )
                  producto.save()
                  return render(request, "App/about.html")
      else:
            miFormulario = ProductoFormulario()
 
      return render(request, "App/cargar_producto.html", {"miFormulario": miFormulario})

#Buscar categoria

def buscar_categoria(request):
    if request.method == "POST":
        mi_formulario = BuscarCategoria(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            categorias = Categoria.objects.filter(nombre__icontains=informacion["nombre"])

            return render(request, "App/mostrar_categoria.html", {"categorias": categorias})
    else:
        mi_formulario = BuscarCategoria()

    return render(request, "App/buscar_categoria.html", {"mi_formulario": mi_formulario}) 