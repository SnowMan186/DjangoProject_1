from django import forms
from .models import Product

FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево",
                   "бесплатно", "обман", "полиция", "радар"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'  # Или нужный класс для дизайна
        self.fields['is_published'].widget.attrs['class'] = 'custom-checkbox'

    def clean_name(self):
        name = self.cleaned_data['name']
        name_lower = name.lower()
        for word in FORBIDDEN_WORDS:
            if word.lower() in name_lower:
                raise forms.ValidationError(f"В названии обнаружено запрещённое слово '{word}'.")
        return name

    def clean_description(self):
        desc = self.cleaned_data['description']
        desc_lower = desc.lower()
        for word in FORBIDDEN_WORDS:
            if word.lower() in desc_lower:
                raise forms.ValidationError(f"В описании обнаружено запрещённое слово '{word}'.")
        return desc

    def clean_price(self):
        price = self.cleaned_data['price']
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price