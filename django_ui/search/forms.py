from django import forms
import csv


class SubmitNeighborhood(forms.Form):

    with open('search/data/nhood_code_names.csv', 'r') as f:
        reader = csv.reader(f)
        NEIGHBORHOODS = []
        for row in reader:
            NEIGHBORHOODS.append(tuple(row))

    code = forms.ChoiceField(label='Select Neighborhood', choices=NEIGHBORHOODS, required=False)


class SubmitAlterations(forms.Form):
    alt_crime = forms.IntegerField(label='New Crime Level (Dangerous Crimes / 100,000 People)',  min_value=0, required=False)
    alt_school = forms.IntegerField(label='New School Quality (0-100)', min_value=0, max_value=100, required=False)
    alt_income = forms.IntegerField(label='New Income Level ($)', min_value=0, required=False)
    alt_cta = forms.ChoiceField(label='Has CTA Station?', choices=[(None, ''), (1, 'Yes'), (0, 'No')], required=False)
