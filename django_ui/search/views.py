from django.shortcuts import render

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


def run(request):
    context = {}
    res = {}
    price = None

    if request.method == 'POST':
        alter_form = SubmitAlterations(request.POST)

        if alter_form.is_valid():
            alt_crime = alter_form.cleaned_data['alt_crime']
            alt_school = alter_form.cleaned_data['alt_school']
            alt_income = alter_form.cleaned_data['alt_income']
            alt_cta = alter_form.cleaned_data['alt_cta']

            price = fetch_new_price(alt_crime, alt_school, alt_income, alt_cta)
    else:
        alter_form = SubmitAlterations()

    context['alter_form'] = alter_form
    if price:
        context['results'] = 'The resulting Median Home Price is: ${:,.2f}'.format(price)

    return render(request, 'index.html', context)
