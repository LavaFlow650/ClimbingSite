from django import forms
from routesetting.models import LogMessage
from routesetting.models import Route

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ("grade", "location", "color", "name", "setter", "date_set")
