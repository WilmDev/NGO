from django.shortcuts import render, redirect
from django.urls import reverse
from event.forms import EventRegistrationForm
from datetime import datetime
from event.models import Event


# Create your views here.
def home(request):
	context = {
		'events': Event.objects.all(),
		'title': 'NGO Event Home'
	}
	return render(request, 'event/home.html', context)


def event_registration(request, id):
	event = Event.objects.filter(id = id).first()
	adult_price = event.ticket_price_adult
	child_price = event.ticket_price_child
	if request.method == "POST":
		form = EventRegistrationForm(request.POST)
		if form.is_valid():
			adult_number = form.cleaned_data['quantity_adult']
			child_number = form.cleaned_data['quantity_child']
			first_name = form.cleaned_data['first_name']
			total = (adult_number*adult_price) + (child_number*child_price)
			total = str(total)
			context = {
				'f_name': first_name,
				'ttl': total
			}
			request.session['context'] = context
			return redirect('registration_success')
			#return render(request, 'event/registration_success.html', context)
	else:
		form = EventRegistrationForm()
	return render (request, 'event/registration.html', {'form': form})


def registration_success(request):	
	context = request.session.get('context')
	return render(request, 'event/registration_success.html', context)

