from django import forms
from .models import Camp, CampYear, get_year_choices
import datetime

class CampForm(forms.ModelForm):

    class Meta:
        model = Camp
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.id:
            self.fields['first_year'] = forms.ChoiceField(
                help_text='The first year your camp will run.',
                choices=get_year_choices(),
                initial=datetime.datetime.now().year
            )




class CampYearForm(forms.ModelForm):
    class Meta:
        model = CampYear
        fields = '__all__'

