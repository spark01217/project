from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def execute(request):
    text = '''
    You have completed the form. Here are your results:
    '''
    return HttpResponse(text)
