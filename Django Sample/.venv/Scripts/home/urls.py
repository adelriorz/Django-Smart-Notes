from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view()),#views.home
    path('authorized', views.AuthorizedView.as_view()),#views.authorized
]
