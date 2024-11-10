from django import forms

from catalog.models import Product
from django.core.exceptions import ValidationError


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]

    stop_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for stop_word in self.stop_words:
            if name.lower() in stop_word:
                raise ValidationError(
                    f"Название товара не должно содержать слово {stop_word}"
                )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for stop_word in self.stop_words:
            if stop_word in description.lower():
                raise ValidationError(f"Описание не должно содержать слово {stop_word}")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Стоимость товара не может быть отрицательной")
        return price


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["is_published"]
