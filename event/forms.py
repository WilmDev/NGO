from django import forms
from event.models import Event, Event_Registration
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EventRegistrationForm(forms.Form):
	first_name = forms.CharField(label='First Name', max_length = 100)
	last_name = forms.CharField(label='Last Name', max_length = 100)
	email_id = forms.EmailField(max_length = 100)
	contact_number = forms.IntegerField()
	address = forms.CharField(max_length = 200)
	quantity_adult = forms.IntegerField()
	quantity_child = forms.IntegerField()




class ConfirmRegistrationForm(forms.Form):
	register = forms.BooleanField(initial = True)