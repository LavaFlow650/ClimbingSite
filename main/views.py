from django.shortcuts import redirect, render
from routesetting.models import Route
from routesetting.views import get_routes_list
from main.forms import FeedbackForm
from django.http import HttpResponse

def get_route():
    pass

def home(request):
    context = {'routes': {'b': {'newest': {}, 'oldest': {}}, 'tr': {'newest': {}, 'oldest': {}}}}

    # get context for newest/oldest routes
    context['b_num'] = Route.objects.filter(type='B', archived__exact=False).count()
    context['tr_num'] = Route.objects.filter(type='T', archived__exact=False).count()
    context['routes']['tr']['oldest'] = Route.objects.filter(type='T').earliest('date_set')
    context['routes']['tr']['newest'] = Route.objects.filter(type='T').latest('date_set')
    context['routes']['b']['oldest'] = Route.objects.filter(type='B').earliest('date_set')
    context['routes']['b']['newest'] = Route.objects.filter(type='B').latest('date_set')

    # get context for route graphs
    context['color_lookup'] = Route.color_lookup
    context['b_list'] = get_routes_list('B')
    context['tr_list'] = get_routes_list('T')
    return render(request, 'main/home.html', context=context)

def view_routes(request):
    pass

def give_feedback(request, route = None):
    form = FeedbackForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            temp = form.save(commit=False)
            if form.data.get("rating_bool") == "on":
                temp.rating = None
            if form.data.get("route") == '':
                temp.rating = None
                temp.grade = None
            temp.save()
            return HttpResponse("thank you for your feedback")
    return render(request, "main/feedback_form.html", {"form": form})