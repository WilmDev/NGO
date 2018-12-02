from django.shortcuts import render
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
	item = Event.objects.filter(id = id).first()
	context = {
		'event': item,
		'title': 'Event registration'
	}
	return render(request, 'event/registration.html', context)

