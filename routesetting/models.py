from django.db import models
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import math

class Route(models.Model):
    location = models.PositiveSmallIntegerField(null=True,blank=True)
    type = models.CharField(max_length=1)
    grade_num = models.IntegerField()
        
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
        "W":"DDDDDD",
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
        TBEAR = "TB", "TBear"
        STEELTOES = "ST", "Steel toes"
        BLACKBEAR = "B", "Blackbear"
    setter = models.CharField(
        max_length=2,
        choices = Setters.choices,
        default = Setters.KB,
    )
    date_set = models.DateField()
    date_logged = models.DateTimeField()
    archived = models.BooleanField()
    archived_date = models.DateTimeField(null=True)

    @property
    def grade(self):
        if self.type == "T":
            pre = "5."
        elif self.type == "B":
            pre = "V"
        else:
            pre = "invalid route type"

        mod = self.grade_num%10
        if mod < 5:
            return pre + str(int(self.grade_num/10))+"+"*mod
        elif mod == 5:
            return pre + "fuck you"
        else:
            return pre + str(1+math.floor(self.grade_num/10))+"-"*(10-mod)

    def __str__(self) -> str:
        return "({}) {}".format(self.grade,self.name)
    
    class Meta:
        ordering = ['grade_num']
    
class RouteFeedback(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, blank=True, null=True)
    feedback = models.CharField(max_length=300, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    grade_int = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField()

    @property
    def grade(self):
        if self.route == None:
            return "None"
        if self.grade_int == None:
            return "bad feedback"
        
        if self.route.type == "T":
            pre = "5."
        elif self.route.type == "B":
            pre = "V"
        else:
            pre = "invalid route type"

        mod = self.grade_int%10
        if mod < 5:
            return pre + str(int(self.grade_int/10))+"+"*mod
        elif mod == 5:
            return pre + "fuck you"
        else:
            return pre + str(1+math.floor(self.grade_int/10))+"-"*(10-mod)