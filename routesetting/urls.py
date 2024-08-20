from django.urls import path
from routesetting import views
from routesetting.models import LogMessage
from routesetting.models import Route

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="routesetting/home.html",
)

# route_list_view = views.RouteListView.as_view(
#     queryset = Route.objects.filter(archived__exact=False).order_by("-date_logged"),
#     context_object_name = "route_list",
#     template_name = "routesetting/view_routes.html",
# )

urlpatterns = [
    path("", home_list_view, name = "home"),
    path("create_route/", views.create_route, name="new_route"),
    path("edit_route/<route_id>", views.edit_route, name="edit_route"),
    path("delete_route/<route_id>", views.delete_route, name="delete_route"),
    path("view_routes/", views.view_routes, name="view_routes"),
    path("import/", views.import_routes_view, name="import"),
    #path("poop/", views.poop, name = "poop"),
    #path("routesetting/<name>", views.hello_there, name="hello_there"),
    #path("about/", views.about, name = "about"),
    #path("contact/", views.contact, name = "contact"),
    #path("log/", views.log_message, name="log"),
]