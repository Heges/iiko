from django.urls import path, reverse

from . import views

app_name = 'dishes'

urlpatterns = [
path('', views.MainListView.as_view(), name='index'),
path('<int:pk>/', views.MainDetailView.as_view(), name='detail'),
path('menu/<slug:slug>/', views.MainCategoryDishes.as_view(), name='categorydishes'),
path('cart/', views.MainCartView.as_view(), name='cartview'),
path('login/', views.MainLoginView.as_view(), name='loginview'),
path('registr/', views.MainRegistrView.as_view(), name='registrview'),
path('logout/', views.MainLogoutView.as_view(), name='logoutview'),
path('remove/<int:pk>/', views.MainCartRemove.as_view(), {'key': 'remove'}, name='cartremoveview'),
path('search_result/', views.MainSerchResult.as_view(), name='searchresultview'),
path('articles/', views.MainArticles.as_view(), name='articlesview'),
path('articles/<int:pk>/', views.MainArticlesDetail.as_view(), name='articlesdetailview'),
path('articles/create/', views.MainArticlesCreate.as_view(), name='articlescreateview'),
path('cart/plusValue/', views.MainCartPlusValue.as_view(), name='plusValueview'),
]
