from django.shortcuts import render
from django.shortcuts import render
from .models import *
from django.apps import apps

# Create your views here.
def index(request):

  
    school_application = apps.get_app_config('school')


    school_models = school_application.get_models()

    # A dictionary for store model names and related fields
    model_dict = {}

    for model in school_models:
        model_name = model.__name__
        fields = [field.name for field in model._meta.get_fields()]
        model_dict[model_name] = fields[1:]
        print(fields)

    school_table = School.objects.all()
    assessment_area_table = AssessmentArea.objects.all()
    awards_table = Award.objects.all()
    class_table = Class.objects.all()
    student_table = Student.objects.all()
    subject_table = Subject.objects.all()
    answer_table = Answer.objects.all()
    category_table = Category.objects.all()
    correct_answer_table = CorrectAnswer.objects.all()
    summary_table = Summary.objects.all()

    return render(request, "school/index.html", {"models": model_dict, "school_table": school_table, "assessment_area_table": assessment_area_table, "awards_table": awards_table, "class_table": class_table, "student_table": student_table, "subject_table": subject_table, "answer_table": answer_table, "category_table": category_table, "correct_answer_table": correct_answer_table, "summary_table": summary_table} )