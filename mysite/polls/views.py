from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
# Create your views here.
def index(request):
    return render(request, "polls/index.html")

def detail(request):
    return render(request, "polls/detail.html")
