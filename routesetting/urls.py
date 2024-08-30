from django.urls import path
from routesetting import views
# from routesetting.models import Route

urlpatterns = [
    path("", views.home, name = "routesetting_home"),
    path("create_route/", views.create_route, name="new_route"),
    path("edit_route/<route_id>", views.edit_route, name="edit_route"),
    path("delete_route/<route_id>", views.delete_route, name="delete_route"),
    path("view_routes/", views.view_routes, name="view_routes"),
    path("import_routes/", views.import_routes_view, name="import routes"),
    path("nico/", views.nico, name="nico"),
]