from django.db import models
from django.utils import timezone
import math

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Route(models.Model):
    location = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=1)
    grade = models.IntegerField()

    @property
    def display_grade(self):
        if self.type == "T":
            pre = "5."
        elif self.type == "B":
            pre = "V"
        else:
            pre = "invalid route type"

        mod = self.grade%10
        if mod < 5:
            return pre + str(int(self.grade/10))+"+"*mod
        elif mod == 5:
            return pre + "fuck you"
        else:
            return pre + str(1+math.floor(self.grade/10))+"-"*(10-mod)
        
    color_lookup = {
        "R":"D22B2B",
        "O":"FF5F1F",
        "Y":"FFEA00",
        "LG":"AAFF00",
        "DG":"355E3B",
        "Bu":"4169E1",
        "Pu":"9400D3",
        "Bk":"111111",
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
        return '{} ({})'.format(self.name,self.display_grade)