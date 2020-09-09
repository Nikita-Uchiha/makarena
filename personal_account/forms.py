from django.contrib.auth.models import User
from django import forms
from .models import CustomUser


class UserLoginForm(forms.Form):
	phone = forms.CharField()
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	

	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
		
		self.fields['phone'].widget.attrs.update({'id': 'second_phone'})
		self.fields['password'].widget.attrs.update({'class': 'code'})


class UserRegistrationForm(forms.Form):
    phone = forms.CharField()

    def __init__(self, *args, **kwargs):
    	super(UserRegistrationForm, self).__init__(*args, **kwargs)
    	self.fields['phone'].widget.attrs.update({'class': 'phone'})




class UserRegistrationForm2(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['address_street', 'address_house', 'address_entrance', 'address_apartment', 'address_floor', 'Birth_Date', 'first_name','email']

	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm2, self).__init__(*args, **kwargs)
		self.fields['address_street'].widget.attrs.update({'class': 'input_PA rfield'})
		self.fields['address_house'].widget.attrs.update({'class': 'input_PA rfield'})
		self.fields['address_entrance'].widget.attrs.update({'class': 'input_PA rfield'})
		self.fields['address_apartment'].widget.attrs.update({'class': 'input_PA rfield'})
		self.fields['address_floor'].widget.attrs.update({'class': 'input_PA rfield'})
		self.fields['Birth_Date'].widget.attrs.update({'class': 'input_PA rfield'})
		self.fields['first_name'].widget.attrs.update({'class': 'input_PA rfield'})
		self.fields['email'].widget.attrs.update({'class': 'input_PA '})
