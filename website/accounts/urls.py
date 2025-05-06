from django.urls import path

from accounts import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("register_success/", views.register_success, name="register_success"),
]
