from django import forms

class OrderForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, max_value=10)
    name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=20)
    size = forms.CharField(max_length=50)

    