from .models import Question
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    questions=Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

def recent_question(request,number):
    questions= Question.objects.order_by("-pub_date")[:number]
    return render(request, 'polls/index.html', {'questions': questions})