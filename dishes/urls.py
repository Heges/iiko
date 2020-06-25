from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'dishes'

urlpatterns = [
path('', views.ListView.as_view(), name='index'),
path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]

