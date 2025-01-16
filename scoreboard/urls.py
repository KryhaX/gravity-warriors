from django.urls import path
from .views import scoreboard_list, new_Dips , new_Pull_ups

urlpatterns = [
    path('', scoreboard_list, name='scoreboard_list'),
    path('new_Dips/', new_Dips, name='new_Dips'),
    path('new_Pull_ups/', new_Pull_ups, name='new_Pull_ups'),

]
