from django import forms

from discover_art.art_products.models import Product


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('quantity', 'user')
#
# class ProductCreateForm(ProductBaseForm):
#     pass
#
class ProductEditForm(ProductBaseForm):
    pass
#
# class ProductDeleteForm(ProductBaseForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for _, field in self.fields.items():
#             field.required = False
#             field.widget.attrs['disabled'] = 'disabled'
#             field.widget.attrs['readonly'] = 'readonly'
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.delete()
#         return self.instance


# class SearchProductForm(forms.Form):
#     product = forms.CharField(
#         max_length=50,
#         required=False,
#         label='Search painting!',
#         widget=forms.TextInput(attrs={'placeholder': 'Search here!'}),
#     )