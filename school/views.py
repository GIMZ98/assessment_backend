from django.shortcuts import render
from django.shortcuts import render
from .models import *
from django.apps import apps

# Create your views here.
def index(request):

    # Get models and their fields
    school_application = apps.get_app_config('school')

    # Get all models from the 'school' app
    school_models = school_application.get_models()

    # A dictionary for store model names and related fields
    model_dict = {}

    for model in school_models:
        model_name = model.__name__
        fields = [field.name for field in model._meta.get_fields()]
        model_dict[model_name] = fields[1:]
        print(fields)


    return render(request, "school/index.html", {"models": model_dict})
