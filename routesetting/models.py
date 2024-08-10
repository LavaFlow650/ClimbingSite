from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Route(models.Model):
    grade    = models.SmallIntegerField()
    location = models.PositiveSmallIntegerField()
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
        return '{} (V{})'.format(self.name,self.grade)