from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SubmitNeighborhood, SubmitAlterations
from .functions_for_django import fetch_new_price, fetch_current_data


def test(request):
    """The home page form. Prompts the user to select a neighborhood to analyze."""
    context = {}
    args = {}

    if request.method == 'POST':
        form = SubmitNeighborhood(request.POST)

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


def home2(request):
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
    context = {}

    if request.method == 'GET':
        select_form = SubmitNeighborhood(request.GET)
        alter_form = SubmitAlterations(request.GET)
    else:
        select_form = SubmitNeighborhood()
        alter_form = SubmitAlterations()

    context['select_form'] = select_form
    context['alter_form'] = alter_form
    context['res'] = fetch_current_data(code)

    return render(request, 'index.html', context)


def alter(request, alt_crime, alt_school, alt_income, alt_cta):
    context = {}
    res = {'crime': alt_crime, 'school': alt_school, 'income': alt_income}

    if alt_cta == 1:
        res['cta'] = 'Yes'
    else:
        res['cta'] = 'No'

    res['price'] = fetch_new_price(alt_crime, alt_school, alt_income, alt_cta)

    if request.method == 'POST':
        select_form = SubmitNeighborhood(request.GET)
        alter_form = SubmitAlterations(request.GET)
        print(request.POST)
    else:
        select_form = SubmitNeighborhood()
        alter_form = SubmitAlterations()

    context['select_form'] = select_form
    context['alter_form'] = alter_form
    context['res'] = res

    return render(request, 'index.html', context)


def home(request):
    return render(request, 'index.html', {})


def calculate(request):
    context = {}

    if request.method == 'POST':
        form = SubmitAlterations(request.POST)

        if form.is_valid():
            alt_crime = int(form.cleaned_data['alt_crime'])
            alt_school = int(form.cleaned_data['alt_school'])
            alt_income = int(form.cleaned_data['alt_income'])
            alt_cta = int(form.cleaned_data['alt_cta'])

            price = fetch_new_price(alt_crime, alt_school, alt_income, alt_cta)

            context['results'] = 'The resulting Median Home Price is: ${:,.2f}'.format(price)
    else:
        form = SubmitAlterations()

    context['form'] = form

    return render(request, 'calculate.html', context)


def lookup(request):
    context = {'results': False}

    if request.method == 'POST':
        form = SubmitNeighborhood(request.POST)

        if form.is_valid():
            code = int(form.cleaned_data['code'])
            res = fetch_current_data(code)

            context['crime'] = 'Crime Level: {}'.format(res['crime'])
            context['school'] = 'School Quality: {}'.format(res['school'])
            context['income'] = 'Income Level: ${:,.2f}'.format(res['income'])

            if res['cta'] == 0:
                has_cta = 'No'
            else:
                has_cta = 'Yes'

            context['cta'] = 'Has CTA Station? ' + has_cta
            context['price'] = 'Median Home Price: ${:,.2f}'.format(res['price'])

            context['results'] = True

    else:
        form = SubmitNeighborhood()

    context['form'] = form

    return render(request, 'lookup.html', context)


