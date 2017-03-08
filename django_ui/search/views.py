from django.shortcuts import render

from .forms import SubmitNeighborhood, SubmitAlterations
from .regression import predict, fetch_current_data


def home(request):
    return render(request, 'index_frames.html', {})


def calculate(request):
    context = {}

    if request.method == 'POST':
        form = SubmitAlterations(request.POST)

        if form.is_valid():
            alt_crime = int(form.cleaned_data['alt_crime'])
            alt_school = int(form.cleaned_data['alt_school'])
            alt_income = int(form.cleaned_data['alt_income'])
            alt_cta = int(form.cleaned_data['alt_cta'])

            price = predict(alt_crime, alt_income, alt_school, alt_cta)

            context['results'] = 'Predicted Median Home Price: ${:,.2f}'.format(price)
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

            context['crime'] = '{:,} (per 100,000 people)'.format(res['crime'])
            context['school'] = '{}%'.format(res['school'])
            context['income'] = '${:,.2f}'.format(res['income'])

            if res['cta'] == 0:
                context['cta'] = 'No'
            else:
                context['cta'] = 'Yes'

            context['price'] = '${:,.2f}'.format(res['price'])

            context['results'] = True

    else:
        form = SubmitNeighborhood()

    context['form'] = form

    return render(request, 'lookup.html', context)
