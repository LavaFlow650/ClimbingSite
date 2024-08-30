from django.urls import path
from model_testing import views

urlpatterns = [
    path("create_route/", views.route_form, name="route_form"),
    path("edit_route/<route_id>", views.route_form),
    path("feedback/", views.feedback, name="feedback"), 
    path("feedback/<route_id>", views.feedback), 
    path("view_feedback/", views.view_feedback, name="view feedback")
]
