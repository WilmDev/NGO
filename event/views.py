from django.shortcuts import render, redirect
from django.urls import reverse
from event.forms import EventRegistrationForm, ConfirmRegistrationForm
from datetime import datetime
from event.models import Event, Event_Registration


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
			last_name = form.cleaned_data['last_name']
			email_id = form.cleaned_data['email_id']
			contact_number = form.cleaned_data['contact_number']
			address = form.cleaned_data['address']
			adult_number = int(form.cleaned_data['quantity_adult'])			
			child_number = int(form.cleaned_data['quantity_child'])
			first_name = form.cleaned_data['first_name']
			total = (adult_number*adult_price) + (child_number*child_price)
			total = str(total)
			context = {
				'event_id': str(id),
				'first_name': first_name,
				'ttl': total,
				'last_name': last_name,
				'email_id': email_id,
				'contact_number': contact_number,
				'address': address,
				'adult_number': adult_number,
				'child_number': child_number,				

			}
			request.session['context'] = context
			return redirect('registration_success')
			#return render(request, 'event/registration_success.html', context)
	else:
		form = EventRegistrationForm()
	return render (request, 'event/registration.html', {'form': form})


def registration_success(request):	
	if request.method == "POST":
		form = ConfirmRegistrationForm(request.POST)
		if form.is_valid():
			context = request.session.get('context')
			customer = Event_Registration()
			customer.event = Event.objects.filter(id = int(context['event_id'])).first()
			customer.first_name = context['first_name']
			customer.last_name = context['last_name']
			customer.email_id = context['email_id']
			customer.contact_number = int(context['contact_number'])
			customer.address = context['address']
			customer.adult_number = int(context['adult_number'])
			customer.child_number = int(context['child_number'])
			customer.first_name = context['first_name']
			customer.save()
			return render(request, 'event/registration_success.html', {'message': "registration complete"})
		else:
			return render(request, 'event/registration_success.html')
						

			context = {
				'f_name': "Kobiltoy",
				'success': "Done"
			}
			return render(request, 'event/registration_success.html', context)
	else:
		form = ConfirmRegistrationForm()
		context = request.session.get('context')
		context.update({'form': form})
		return render(request, 'event/registration_success.html', context)
			
	
	

