from django.urls import path

from . import views

app_name = 'dishes'

urlpatterns = [
path('', views.MainListView.as_view(), name='index'),
path('<int:pk>/', views.MainDetailView.as_view(), name='detail'),
path('menu/<slug:slug>/', views.MainCategoryDishes.as_view(), name='categorydishes'),
path('cart/', views.MainCartView.as_view(), name='cartview'),
path('login/', views.MainLoginView.as_view(), name='loginview'),
path('registr/', views.MainRegistrView.as_view(), name='registrview'),
]
