from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}

    ordering = 'group'
    students_objects = Student.objects.all().order_by(ordering)
    context['object_list'] = students_objects

    return render(request, template, context)
