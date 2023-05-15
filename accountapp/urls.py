from django.urls import path
from . import views
from accountapp.views import hello_world

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('', views.post_list, name='post_list'),
]