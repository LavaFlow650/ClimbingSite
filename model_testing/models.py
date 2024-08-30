from django.db import models
import math

# Create your models here.

class Route(models.Model):
    name = models.CharField(max_length=100)
    grade_num = models.IntegerField()
    type = models.CharField(max_length=1)
    
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