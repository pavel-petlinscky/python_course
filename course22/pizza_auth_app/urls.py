from django.urls import path

from django.contrib.auth.views import logout_then_login, LoginView
from django.views.generic import CreateView

from pizza_auth_app.forms import CustomCreationForm

app_name = 'pizza_auth_app'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='auth_app/login.html'
    ), name='login'),

    path('logout/', logout_then_login, name='logout'),

    path('register/', CreateView.as_view(
        template_name='auth_app/register.html',
        form_class=CustomCreationForm,
        success_url='/',
    ), name='register'),
]
