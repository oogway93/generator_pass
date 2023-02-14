from django.urls import path
from . import views

urlpatterns = [
    path('', views.generator_pass),
]
