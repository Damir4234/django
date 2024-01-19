from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category',
                  'image', 'purchase_price',)
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_list = ['казино', 'криптовалюта', 'крипта',
                           'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for obj in prohibited_list:
            if obj in cleaned_data:
                raise forms.ValidationError("Продукт запрещен на площадке")

        return cleaned_data


class ModeratorProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for obj in prohibited_list:
            if obj in cleaned_data:
                raise forms.ValidationError("Продукт запрещен на площадке")

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'name', 'number_version', 'current_version',)
