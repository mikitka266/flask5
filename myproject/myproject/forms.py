from django import forms
from models import Product


class ImageForm(forms.Form):
    image = forms.ImageField()
    product_image = Product.forms.ImageField()