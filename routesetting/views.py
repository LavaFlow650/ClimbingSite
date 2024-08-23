from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
from django.shortcuts import redirect

from routesetting.models import Route
from routesetting.forms import RouteForm

from operator import itemgetter

#from routesetting.import_routes import *

# Create your views here.

def home(request):
    return render(request, "routesetting/home.html")

def get_routes_list(type):
    return list(Route.objects.filter(archived__exact=False, type=type).order_by('color').values_list("grade", "color", "name"))


def delete_route(request, route_id):
    Route.objects.filter(id=route_id).delete()
    return redirect("view_routes")

def view_routes(request):
    # if request.method == "POST":
    #     Route.objects.filter(id=request.POST['delete']).delete()
    if request.user_agent.is_mobile:
        print("hon hon hor ")
    context = {}
    context['tr_obj'] = Route.objects.filter(archived__exact=False, type="T").order_by("grade")
    context['b_obj'] = Route.objects.filter(archived__exact=False, type="B").order_by("grade")
    context['color_lookup'] = Route.color_lookup
    context['b_list'] = get_routes_list('B')
    context['tr_list'] = get_routes_list('T')
    return render(request, "routesetting/view_routes.html", context)

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

def nico(request):
    form = RouteForm(None)
    return render(request, "routesetting/nico_home.html", {"form": form})

# def import_routes_view(request):
#     csv_file_path = '/Users/k1einbottle/Documents/code/Github/ClimbingSite/test.csv'  # Replace with your actual file path
#     import_routes(csv_file_path)
#     return redirect('view_routes')