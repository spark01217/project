from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from .forms import SubmitNeighborhood, SubmitAlteredParameters


def start(request):
    form = SubmitNeighborhood()
    context = {}
    # args = {}
    # args['neighborhood'] = form.cleaned_data['neighborhood']
    context = {'form': form}

    return render(request, 'index.html', context)

# def alter(request, neighborhood):
    # form = SubmitAlteredParameters()
    # context['form'] = form
    # return
