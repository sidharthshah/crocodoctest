from django.views.generic.edit import CreateView
from frontend.models import Example
from frontend.forms import ExampleForm


class ExampleCreate(CreateView):
    model = Example
    form_class = ExampleForm
    fields = ['name', 'file']
    success_url = "/example/success"
