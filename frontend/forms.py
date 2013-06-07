from django.forms import ModelForm
from .models import Example


class ExampleForm(ModelForm):
    class Meta:
        model = Example
