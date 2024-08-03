from django.urls import path
from . import views

urlpatterns = [
    path('', views.form),
    path('postform', views.post_form),
]