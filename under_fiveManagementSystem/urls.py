

from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('manage_child', views.manageChildren, name="manage_child"),
    path('add_child', views.Add_Child,name='add_child'),
    path("age_rage", views.Child_age_range, name="age_range")
    
]
