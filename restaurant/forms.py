from django import forms
from restaurant.models import RestaurantModel


class RestaurantForm(forms.ModelForm):
    restro_name = forms.CharField(label="Restaurent Name")
    restro_contact = forms.IntegerField(label="Contact")
    restro_email = forms.EmailField(label="Email")
    restro_area = forms.CharField(label="Area")
    restro_type = forms.CharField(label="Restaurant Type")
    restro_password = forms.CharField(max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = RestaurantModel
        fields = "__all__"
        exclude = ('restro_id', 'restro_otp', 'restro_status')
