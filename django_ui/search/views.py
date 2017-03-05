from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pandas as pd

from .forms import SubmitNeighborhood, SubmitAlterations
from .models import Neighborhood

import merge

def test(request):
    """The home page form. Prompts the user to select a neighborhood to analyze."""
    context = {}
    args = {}

    if request.method == 'GET':
        form = SubmitNeighborhood(request.GET)

        if form.is_valid():
            args['neighborhood_code'] = form.cleaned_data['neighborhood_code']
            args['alt_crime'] = form.cleaned_data['alt_crime']
            args['alt_school'] = form.cleaned_data['alt_school']
            args['alt_income'] = form.cleaned_data['alt_income']
            args['alt_CTA'] = form.cleaned_data['alt_CTA']

    else:
        form = SubmitNeighborhood()

    context['form'] = form

    return render(request, 'index.html', context)


def home(request):
    """Shows all the forms."""
    context = {}

    if request.method == 'GET':
        select_form = SubmitNeighborhood(request.GET)
    else:
        select_form = SubmitNeighborhood()

    context['select_form'] = select_form
    context['alter_form'] = None
    context['res'] = None

    return render(request, 'index.html', context)


def fetch(request, code):
    res = {}
    context = {}

    df = pd.read_csv('search/data/current_data.csv')
    row = df[(df['community'] == code) & (df["date"] == 2016)]

    res['crime'] = int(row.iloc[0]['crime_freq'])
    res['school'] = int(row.iloc[0]['score'])
    res['income'] = int(row.iloc[0]['income'])
    res['price'] = int(row.iloc[0]['value'])

    if int(row.iloc[0]['cta']) == 1:
        res['cta'] = 'Yes'
    else:
        res['cta'] = 'No'

    if request.method == 'GET':
        select_form = SubmitNeighborhood(request.GET)
        alter_form = SubmitAlterations(request.GET)
    else:
        select_form = SubmitNeighborhood()
        alter_form = SubmitAlterations()

    context['select_form'] = select_form
    context['alter_form'] = alter_form
    context['res'] = res

    return render(request, 'index.html', context)


def alter(request, code, alt_crime, alt_school, alt_income, alt_cta):

    res = {'crime': alt_crime, 'school': alt_school, 'income': alt_income}

    if alt_cta == 1:
        res['cta'] = 'Yes'
    else:
        res['cta'] = 'No'

    res['price'] = predict(code, alt_crime, alt_school, alt_income, alt_cta)

    return
