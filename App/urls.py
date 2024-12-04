from django.urls import path
from App import views 

urlpatterns = [
   path('',views.inicio, name="Inicio"),
   path('about/',views.about, name="About"),
   path('projects/',views.projects, name="Projects"),
   path('signup/',views.signup, name="Signup")
]

