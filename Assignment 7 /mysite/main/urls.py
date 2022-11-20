from django.urls import path
from . import views

 

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('update/<str:a>/', views.update, name="update"),
    path('delete/<str:a>/', views.delete, name="delete"),
    path('sname', views.sname, name="sname"),
    path('sprofession', views.sprofession, name="sprofession"),
    path('compare', views.compare, name="compare"),
]

