from django import forms
from .models import Product, Category, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('users_wishlist',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        c_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        brands = Brand.objects.all()
        b_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = c_friendly_names
        self.fields['brand'].choices = b_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-secondary'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = "__all__"
