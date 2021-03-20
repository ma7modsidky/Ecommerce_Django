from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label= _('Quantity'))
    override = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class CartAddProductForm2(forms.Form):
    quantity = 1
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
