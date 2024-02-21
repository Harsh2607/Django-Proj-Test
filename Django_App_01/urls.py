from django.urls import path, include
from Django_App_01 import views

# Template URLs
app_name = "Django_App_01"

urlpatterns = [
    path("form-page/", views.input_form_view, name="input_form"),
    path("model-form/", views.input_model_form, name="model_form"),
    path("register/", views.user_register, name="user_register"),
    path("user-login", views.user_login, name="user_login"),
    path("", views.albums, name="albums"),
]