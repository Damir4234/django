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

    version_name = forms.CharField(
        max_length=100, required=False, label='Имя версии')
    version_number = forms.IntegerField(required=False, label='Номер версии')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.id:
            # Если объект еще не создан (редактирование), скрываем поля версии
            self.fields['version_name'].widget = forms.HiddenInput()
            self.fields['version_number'].widget = forms.HiddenInput()

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_list = ['казино', 'криптовалюта', 'крипта',
                           'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for obj in prohibited_list:
            if obj in cleaned_data:
                raise forms.ValidationError("Продукт запрещен на площадке")

        return cleaned_data

    def save(self, commit=True):
        product = super().save(commit=False)

        version_name = self.cleaned_data.get('version_name')
        version_number = self.cleaned_data.get('version_number')

        if version_name and version_number:
            version = Version.objects.create(
                product=product,
                name=version_name,
                number_version=version_number,
                current_version=True,
            )
            product.versions.add(version)

        if commit:
            product.save()

        return product


class CreateProductForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['version_name'].widget = forms.HiddenInput()
        self.fields['version_number'].widget = forms.HiddenInput()


class EditProductForm(ProductForm):
    pass


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
        fields = ('name', 'number_version', 'current_version',)
