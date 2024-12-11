from django.urls import path
from App import views 

urlpatterns = [
   path('',views.inicio, name="Inicio"),
   path('about/',views.about, name="About"),
   path('projects/',views.projects, name="Projects"),
   path('signup/',views.signup, name="Signup")
]

forms = [
    path('cargar_categoria/',views.cargar_categoria, name="CargarCategoria"),
    path('cargar_subcategoria/',views.cargar_subcategoria, name="CargarSubCategoria"),
    path('cargar_producto/',views.cargar_producto, name="CargarProducto"),
    path('buscar_categoria/',views.buscar_categoria, name="FormBuscarCategoria"),
    
]

urlpatterns += forms