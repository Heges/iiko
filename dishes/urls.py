from django.urls import path

from . import views

app_name = 'dishes'

urlpatterns = [
path('', views.MainListView.as_view(), name='index'),
path('<int:pk>/', views.MainDetailView.as_view(), name='detail'),
path('<slug:slug>/', views.MainCategoryDishes.as_view(), name='categorydishes'),
#path('<slug:slug>/menu', views.MainMenuView, name='menu'),
]
