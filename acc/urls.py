from django.urls import path
from . import views

app_name = "acc"
urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.userlogin, name="login"),
    path('logout', views.userlogout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('update', views.update, name="update"),
    path('remove', views.remove, name="remove")
]