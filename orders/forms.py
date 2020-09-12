from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address_street', 'address_house', 'address_entrance', 'address_apartment', 'address_floor', 'bonus_card', 'comment']

    def __init__(self, *args, **kwargs):
    	super(OrderCreateForm, self).__init__(*args, **kwargs)
    	self.fields['comment'].widget = forms.Textarea()
    	self.fields['address_street'].widget.attrs.update({'class': 'street_entry rfield'})
    	self.fields['address_house'].widget.attrs.update({'class': 'house_entry rfield'})
    	self.fields['address_entrance'].widget.attrs.update({'class': 'padick_entry rfield'})
    	self.fields['address_apartment'].widget.attrs.update({'class': 'flet_entry rfield'})
    	self.fields['address_floor'].widget.attrs.update({'class': 'floor_entry rfield'})
    	self.fields['bonus_card'].widget.attrs.update({'class': 'checkbox'})
    	self.fields['comment'].widget.attrs.update({'class': 'comment_entry '})
        

