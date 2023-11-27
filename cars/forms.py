from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['seller','created_date','is_featured',]

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['year'].widget = forms.Select(choices=Car.year_choice)
        self.fields['features'].widget = forms.CheckboxSelectMultiple(choices=Car.features_choices)
        self.fields['doors'].widget = forms.Select(choices=Car.door_choices)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
