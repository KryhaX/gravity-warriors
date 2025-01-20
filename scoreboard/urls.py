from django.urls import path

from .views import scoreboard_list, new_Dips , new_Pull_ups, edit_Dips, edit_Pull_ups, delete_Dips, delete_Pull_ups

urlpatterns = [
    path('', scoreboard_list, name='scoreboard_list'),
    path('new_Dips/', new_Dips, name='new_Dips'),
    path('new_Pull_ups/', new_Pull_ups, name='new_Pull_ups'),

    path('edit_Dips/<int:dip_id>/', edit_Dips, name='edit_Dips'),
    path('edit_Pull_ups/<int:pullups_id>/', edit_Pull_ups, name='edit_Pull_ups'),

    path('delete_Dips/<int:dip_id>/', delete_Dips, name='delete_Dips'),
    path('delete_Pull_ups/<int:pullups_id>/', delete_Pull_ups, name='delete_Pull_ups'),

]
