


from django.urls import path, re_path
from .views import Registration,Login
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    # path('login', views.Logi
    path('register',csrf_exempt(Registration.as_view()),name="register"),
    path('login',csrf_exempt(Login.as_view()),name="login"),

    
]