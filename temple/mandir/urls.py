from django.urls import path
from .views.main_views import add_event,event_list

urlpatterns = [
    path('add_event/',add_event,name='add_event'),
    path('event_list/',event_list,name='event_list'),
]
