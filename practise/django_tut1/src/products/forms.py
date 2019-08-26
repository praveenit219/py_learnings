from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """ title = forms.CharField(
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': 'your title'
                        }
                    )) """
    #title  = forms.CharField()
    #email = forms.EmailField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    """
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')       
        if not 'cfe' in title:
            raise forms.ValidationError('This is not a valid input')       
        return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')       
        if not email.endswith('edu'):
            raise forms.ValidationError('This is not a valid email')       
        return email
    """

class RawProductForm(forms.Form):
    """ title = forms.CharField(
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': 'your title'
                        }
                    )) """
    title = forms.CharField()
    description = forms.CharField(
                    widget=forms.Textarea(
                        attrs={
                            'placeholder': 'your description',
                            'class': 'new-class-name two',
                            'id': 'my-id-for-textarea',
                            'rows': 5,
                            'cols': 60
                        }))
    price = forms.DecimalField()