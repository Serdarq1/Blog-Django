from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search/', views.BlogSearchView.as_view(), name='search_blogs'),
    path('<slug:slug>/', views.DetailView.as_view(), name='post_list'),
]
