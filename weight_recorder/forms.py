from django import forms

from .models import Weight


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ('weight_value', 'weight_date')
