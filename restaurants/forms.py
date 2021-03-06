from django import forms

from .models import Restaurant


class SearchForm(forms.Form):
    # See: https://docs.djangoproject.com/en/dev/ref/models/fields/#field-choices
    # and: https://stackoverflow.com/questions/8859504/django-form-dropdown-list-of-numbers
    price_range = forms.ChoiceField(Restaurant.get_price_range_choices, required=False)
    neighborhood = forms.ChoiceField(Restaurant.get_neighborhood_choices, required=False)
    category = forms.ChoiceField(Restaurant.get_category_choices, required=False)

    # def clean(self):
    #     cleaned_data = super(SearchForm, self).clean()
    #     price_range = cleaned_data.get('price_range')
    #     neighborhood = cleaned_data.get('neighborhood')
    #     category = cleaned_data.get('category')
        # if not price_range and not neighborhood and not category:
        #     raise forms.ValidationError(
        #         'You must select a value for all inputs!'
        #     )

class SelectForm(forms.Form):
    # See: https://docs.djangoproject.com/en/dev/ref/models/fields/#field-choices
    # and: https://stackoverflow.com/questions/8859504/django-form-dropdown-list-of-numbers
    name = forms.ChoiceField(Restaurant.get_name_choices, required=False)
