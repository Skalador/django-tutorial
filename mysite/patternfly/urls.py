from django.urls import path

from . import views

app_name = "patternfly"
urlpatterns = [
    #path('', views.home, name='home'),  # Home page
    path("", views.IndexView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
]
