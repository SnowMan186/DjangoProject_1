from django import forms
from .models import Product

FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево",
                     "бесплатно", "обман", "полиция", "радар"]

class ProductForm(forms.ModelForm):
      class Meta:
          model = Product
          fields = ['name', 'description', 'price', 'is_published']

      def clean_name(self):
          name = self.cleaned_data['name'].lower()
          for word in FORBIDDEN_WORDS:
              if word.lower() in name:
                  raise forms.ValidationError(f"В названии обнаружено запрещённое слово '{word}'.")
          return name

      def clean_description(self):
          desc = self.cleaned_data['description'].lower()
          for word in FORBIDDEN_WORDS:
              if word.lower() in desc:
                  raise forms.ValidationError(f"В описании обнаружено запрещённое слово '{word}'.")
          return desc

      def clean_price(self):
          price = self.cleaned_data['price']
          if price < 0:
              raise forms.ValidationError("Цена не может быть отрицательной.")
          return price

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_published'].widget.attrs.update({'class': 'custom-checkbox'})

