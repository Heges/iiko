from django.urls import path
from . import views

app_name = 'dishes'

urlpatterns = [
path('', views.IndexView, name = 'index'),
path('<slug:slug>/', views.DetailView.as_view(), name= 'detail'),
]