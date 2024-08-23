from django.db import models
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import math

class Route(models.Model):
    location = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=1)
    grade = models.IntegerField()
        
    color_lookup = {
        "R":"D22B2B",
        "O":"FF5F1F",
        "Y":"FFEA00",
        "LG":"AAFF00",
        "DG":"355E3B",
        "Bu":"4169E1",
        "Pu":"9400D3",
        "Bk":"333333",
        "Pi":"FF00FF",
        "W":"DDDDDD"
    }
    class Colors(models.TextChoices):
        RED =         "R", "Red"
        ORANGE =      "O", "Orange"
        YELLOW =      "Y", "Yellow"
        LIGHT_GREEN = "LG", "Light green"
        DARK_GREEN =  "DG", "Dark green"
        BLUE =        "Bu", "Blue"
        PURPLE =      "Pu", "Purple"
        BLACK =       "Bk", "Black"
        PINK =        "Pi", "Pink"
        WHITE =       "W", "White"
    color = models.CharField(
        max_length = 2,
        choices = Colors.choices,
        default = Colors.RED
    )
    name = models.CharField(max_length=100)
    class Setters(models.TextChoices):
        KB = "K", "KB"
        APE = "A", "APE"
        OK = "O", "OK"
        TOPS = "T", "TOPS"
        FIREWX = "F", "firewx"
        MERM = "M", "Merm"
        SUNNY = "S", "Sunny"
        CHALK = "C", "Chalk Snorter"
        MAC = "MD", "McDeee"
    setter = models.CharField(
        max_length=2,
        choices = Setters.choices,
        default = Setters.KB,
    )
    date_set = models.DateField()
    date_logged = models.DateTimeField()
    archived = models.BooleanField()
    archived_date = models.DateTimeField(null=True)

    def __str__(self):
        return '{} ({})'.format(self.name)
    
class RouteFeedback(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    sugested_grade = models.IntegerField()
    feedback = models.CharField(max_length=350)