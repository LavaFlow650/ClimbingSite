from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
from django.shortcuts import redirect
from routesetting.forms import LogMessageForm
from routesetting.models import LogMessage
from routesetting.forms import RouteForm
from routesetting.models import Route
from django.views.generic import ListView

# Create your views here.

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
    
class RouteListView(ListView):
    model = Route

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "routesetting/log_message.html", {"form": form})
    
def get_route_dic(id): 
    route_dic = vars(Route.objects.get(id=id))
    keys_to_clean = ['_state', 'archived', 'archived_date']
    for k in keys_to_clean:
        route_dic.pop(k, None)
    return route_dic

def create_route(request):
    form = RouteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            route = form.save(commit=False)
            route.date_logged = datetime.now()
            route.archived = False
            route.save()
            return redirect("view_routes")
    else:
        return render(request, "routesetting/create_route.html", {"form": form})

def edit_route(request, route_id):
    route_id = route_id[1:]
    route_dic = get_route_dic(route_id)
    form = RouteForm(request.POST or None, initial=route_dic)
    if request.method == "POST":
        if form.is_valid():
            route = form.save(commit=False)
            #route.date_logged = datetime.now()
            route.archived = False
            print(route.id)
            route.save()
            return redirect("view_routes")
    else:
        return render(request, "routesetting/create_route.html", {"form": form})
