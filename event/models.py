from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# Create your models here.
class Event(models.Model):
	event_name = models.CharField(max_length = 100)
	event_description = models.TextField()
	event_category = models.CharField(max_length = 100)
	event_start_date = models.DateTimeField()
	event_end_date = models.DateTimeField()
	event_start_time = models.TimeField()
	event_end_time = models.TimeField()
	event_location = models.CharField(max_length = 100)
	ticket_price_adult = models.DecimalField(max_digits=6, decimal_places=2)
	ticket_price_child = models.DecimalField(max_digits=6, decimal_places=2)
	registration_status = models.BooleanField(default=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	

	def __str__(self):
		return self.event_name
