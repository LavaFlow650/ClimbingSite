from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("feedback/",views.give_feedback, name="feedback")
]