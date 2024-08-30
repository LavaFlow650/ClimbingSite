from typing import Any
from django import forms
from model_testing import models
from model_testing.widgets import RateWidget
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class GradeNumField(forms.Field):
    # converts string to grade int (same for tr and boulder)
    def to_python(self, route_str):
        if route_str == '':
            return None

        if route_str[:2] == "5.":
            route_str = route_str[2:]
        elif route_str[:1].lower() == "v":
            route_str = route_str[1:]
        num = 0
        for char in route_str:
            if char.isdigit():
                num = num * 10 + int(char) * 10
            elif char == "+":
                num += 1
            elif char == "-":
                num -= 1
            else:
                raise ValidationError(
                    _("Unknown character %(value)s"),
                    code="invalid",
                    params={"value":char}
                )
        return num
    
    def validate(self, value: Any):
        super().validate(value)
        if value == None:
            return
        if value > 170:
            raise ValidationError(
                _("Grade too large: %(value)s"), 
                code="invalid",
                params={"value": value},
            )
        if value < -1:
            raise ValidationError(
                _("Grade too small: %(value)s"), 
                code="invalid",
                params={"value": value},
            )
    

class GradeTypeField(forms.CharField):
    def validate(self, value: Any):
        super().validate(value)
        if value != "T" and value != "B":
            raise ValidationError(
                _("Invalid route type: %(value)s"), 
                code="invalid",
                params={"value": value},
            )
        
        
class RouteForm(forms.ModelForm):

    def clean(self):
        super().clean()
        route_type = self.cleaned_data.get("type")
        raw_grade = self.data.get("grade_num")

        if route_type == "T" and raw_grade[0] == "V":
            raise ValidationError("Top rope grades can not start with V")
        if route_type == "B" and raw_grade[:2] == "5.":
            raise ValidationError("Boulder grades can not start with 5.")

    class Meta:
        model = models.Route
        fields = ("grade_num", "type", "name")
        field_classes = {
            "grade_num": GradeNumField,
            "type": GradeTypeField,
        }


class RatingField(forms.Field):
    widget = RateWidget()

    def to_python(self, rating):
        return int(float(rating)*2)
    
    def validate(self, value: Any):
        super().validate(value)
        if value>10:
            raise ValidationError(
                _("Rating too large: %(value)s"), 
                code="invalid",
                params={"value": value},
            )
        if value<0:
            raise ValidationError(
                _("Rating too small: %(value)s"), 
                code="invalid",
                params={"value": value},
            )


class FeedbackForm(forms.ModelForm):
    rating_bool = forms.BooleanField(label="No rating", initial="on", required=False)
    
    def clean(self):
        super().clean()
        raw_grade = self.data.get("grade")

        if raw_grade == '':
            return
        
        if self.data.get("route") == '':
            return
        route_type = self.cleaned_data.get("route").grade_type

        if route_type == "T" and raw_grade[0] == "V":
            raise ValidationError("Top rope grades can not start with V")
        if route_type == "B" and raw_grade[:2] == "5.":
            raise ValidationError("Boulder grades can not start with 5.")

    class Meta:
        model = models.RouteFeedback
        fields = ("route", "feedback", "rating", "grade_int")
        field_classes = {
            "rating": RatingField,
            "grade_int": GradeNumField,
            # "grade_num": GradeNumField,
            # "grade_type": GradeTypeField,
        }
        # widgets = {
        #     "rating": RateWidget(),
        # }
    field_order = ['route', 'feedback', 'rating_bool', 'rating', 'grade_int']
        