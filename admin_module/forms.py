from django import forms
from admin_module.models import *


class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = ('state_name',)


class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = "__all__"


class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = "__all__"


class RestaurantTypeForm(forms.ModelForm):
    class Meta:
        model = RestaurantTypeModel
        fields = "__all__"