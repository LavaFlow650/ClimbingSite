from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
from django.shortcuts import redirect
from routesetting.forms import LogMessageForm
from routesetting.models import LogMessage

from routesetting.models import Route
from routesetting.forms import RouteForm

from django.views.generic import ListView

from operator import itemgetter

from routesetting.import_routes import *

# Create your views here.

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
    
def get_routes_list(type):
    return list(Route.objects.filter(archived__exact=False, type=type).values_list("grade", "type", "color", "name"))
    #routes = [(2, 'W'), (2, 'W'), (2, 'W'), (6, 'LG'), (7, 'LG'), (10, 'Y'), (1, 'W')]
    # max_grade = max(routes, key=itemgetter(0))[0]
    # color_dist = {}
    # for route in routes:
    #     if not route[1] in color_dist:
    #         color_dist[route[1]] = [0]*(max_grade+1)
    #     color_dist[route[1]][route[0]] += 1
    # return color_dist

# class RouteListView(ListView):
#     model = Route

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['route_dist'] = get_route_dist()
#         context['color_lookup'] = Route.color_lookup
#         return context

def delete_route(request, route_id):
    Route.objects.filter(id=route_id).delete()
    return redirect("view_routes")

def view_routes(request):
    # if request.method == "POST":
    #     Route.objects.filter(id=request.POST['delete']).delete()
    context = {}
    context['tr_obj'] = Route.objects.filter(archived__exact=False, type="T").order_by("grade")
    context['b_obj'] = Route.objects.filter(archived__exact=False, type="B").order_by("grade")
    context['color_lookup'] = Route.color_lookup
    context['b_list'] = get_routes_list('B')
    context['tr_list'] = get_routes_list('T')
    return render(request, "routesetting/view_routes.html", context)

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
    return render(request, "routesetting/create_route.html", {"form": form})

def edit_route(request, route_id):
    route_base = Route.objects.get(id = route_id)
    initial = {"grade": route_base.display_grade}
    form = RouteForm(request.POST or None, instance=route_base, initial=initial)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("view_routes")
    return render(request, "routesetting/create_route.html", {"form": form})

def import_routes_view(request):
    csv_file_path = '/Users/k1einbottle/Documents/code/Github/ClimbingSite/test.csv'  # Replace with your actual file path
    import_routes(csv_file_path)
    return redirect('view_routes')