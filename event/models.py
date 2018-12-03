from django.db import models
from django.utils import timezone
from datetime import datetime
from ngo import settings 
from django.contrib.auth.models import User





# Create your models here.
class Event(models.Model):
	CONFERENCE = 'CNF'
	SEMINAR = 'SMR'
	PRESENTATION = 'PRS'
	RELIGIOUS = 'RGS'
	SPIRITUAL = 'SPR'
	SOCIAL = 'SCL'
	GENERAL = 'GNR'

	categories = (
		(CONFERENCE, 'Conference'),
		(SEMINAR, 'Seminar'),
		(PRESENTATION, 'Presentation'),
		(RELIGIOUS, 'Religious'),
		(SPIRITUAL, 'Spiritual'),
		(SOCIAL, 'Social'),
		(GENERAL, 'Not Specified')
		)


	event_name = models.CharField(max_length = 100)
	event_description = models.TextField()
	event_category = models.CharField(max_length = 100, choices=categories, default=GENERAL)
	event_start_date = models.DateField()
	event_end_date = models.DateField()
	event_start_time = models.TimeField()
	event_end_time = models.TimeField()
	event_location = models.CharField(max_length = 100)
	ticket_price_adult = models.DecimalField(max_digits=6, decimal_places=2)
	ticket_price_child = models.DecimalField(max_digits=6, decimal_places=2)
	open_for_registration = models.BooleanField(default=True)
	event_requested = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,)
	event_image = models.ImageField(upload_to='event_pics', blank=True)

	

	def __str__(self):
		return self.event_name

class Event_Registration(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	email_id = models.EmailField(max_length = 100)
	contact_number = models.IntegerField(null=True)
	address = models.TextField()
	quantity_adult = models.IntegerField(null=True)
	quantity_child = models.IntegerField(null=True)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)

	def __str__(self):
		return self.event.event_name


