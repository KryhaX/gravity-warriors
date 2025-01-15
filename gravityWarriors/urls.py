from django.contrib import admin
from django.urls import path, include
from scoreboard.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('scoreboard/' ,include('scoreboard.urls')),
    path('', home, name='home'),
]
