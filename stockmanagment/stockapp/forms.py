from django import forms
from.models import Stocks
class Stockforms(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ['categories', 'item_name', 'quantity']
    def clean(self):
        cleaned_data = super().clean()
        categories = cleaned_data.get('categories')  # Check this line
        item_name = cleaned_data.get('item_name')    # And this line
        
        if not categories:
            self.add_error('categories', 'This field is required')
        
        if not item_name:
            self.add_error('item_name', 'This field is required')
        
        return cleaned_data
class searchform(forms.ModelForm):
    class Meta: 
        model = Stocks
        fields = ['item_name','categories']