# Create a form for stock portfolio

# import forms system for django
from django import forms
from .models import Crypto

# create class for stock form
class CryptoForm(forms.ModelForm):
	class Meta:
		model = Crypto
		fields = ["ticker"] # python list# Create a form for stock portfolio
