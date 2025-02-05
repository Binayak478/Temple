from django.urls import path
from .views.main_views import add_event,event_list,list_committee,list_member,add_committee
from .views.auth_views import login

urlpatterns = [
    #auth
    path("login/",login,name="login"),
    
    
    #main
    path('add_event/',add_event,name='add_event'),
    path('event_list/',event_list,name='event_list'),
    path('list_committee/',list_committee,name='list_committee'),
    path("list_member/",list_member,name='list_member'),
    path("add_committee/",add_committee,name='add_committee'),
    
]
