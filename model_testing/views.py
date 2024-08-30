from django.shortcuts import redirect, render
from django.http import HttpResponse
from model_testing.models import RouteFeedback
from model_testing.forms import RouteForm, FeedbackForm

print("http://127.0.0.1:8000/testing/create_route")
print("http://127.0.0.1:8000/testing/edit_route/1")

# Create your views here.

def view_feedback(request):
    context = {}
    context['feedback_list'] = RouteFeedback.objects.order_by("id")
    return render(request, "model_testing/view_feedback.html", context=context)

def route_form(request, route_id = None):
    form = RouteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("view_routes")  
    return render(request, "model_testing/grade_form.html", {"form": form})

def feedback(request, route_id = None):
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
            return redirect("view feedback")
    return render(request, "model_testing/feedback_form.html", {"form": form})
