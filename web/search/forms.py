from django import forms


NEIGHBORHOODS = ['Hyde Park', 'Loop', 'Gold Coast']


class SubmitNeighborhood(forms.Form):
    NEIGHBORHOODS = ['Hyde Park', 'Loop', 'Gold Coast']

    neighborhood = forms.ChoiceField(label='Select Neighborhood',
                                        choices=NEIGHBORHOODS)


class SubmitAlteredParameters(forms.Form):
    alt_crime = forms.IntegerField()
    alt_school = forms.IntegerField(min_value=0, max_value=100)
