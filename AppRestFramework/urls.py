

from django.urls import path , include
from . import views
from AppRestFramework.views import external_api_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [

path("external", views.external_api_view, name="external_api_view"),
]
