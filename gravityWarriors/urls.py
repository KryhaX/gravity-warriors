from django.contrib import admin
from django.urls import path, include
from scoreboard.views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scoreboard/' ,include('scoreboard.urls') , name='scoreboard'),
    path('', home, name='home'),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

]
