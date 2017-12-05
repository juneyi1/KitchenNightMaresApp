from django import forms


class SearchForm(forms.Form):
    price_range = forms.CharField(max_length=5)
    neighborhood = forms.CharField(max_length=50)
    category = forms.CharField(max_length=30)

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        price_range = cleaned_data.get('price_range')
        neighborhood = cleaned_data.get('neighborhood')
        category = cleaned_data.get('category')
        if not price_range and not neighborhood and not category:
            raise forms.ValidationError(
                'You must select a value for all inputs!'
            )
