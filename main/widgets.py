from django.forms.widgets import Input
from django.template import loader
from django.utils.safestring import mark_safe


class RateWidget(Input):
    input_type = "range"
    template_name = "main/widgets/rate_widget.html"