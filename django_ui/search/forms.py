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
    alt_crime = forms.IntegerField(label='Crime Level',
                                   min_value=0,
                                   required=True,
                                   help_text='(Dangerous Crimes / 100,000 People)')
    alt_school = forms.IntegerField(label='School Quality',
                                    min_value=0,
                                    max_value=100,
                                    required=True,
                                    help_text='(0-100)')
    alt_income = forms.IntegerField(label='Income Level',
                                    min_value=0,
                                    required=True,
                                    help_text='(Median Household Income)')
    alt_cta = forms.ChoiceField(label='Has CTA Station?',
                                choices=[(1, 'Yes'), (0, 'No')],
                                required=True)
