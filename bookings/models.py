from django.db import models
from cloudinary.models import CloudinaryField


CABIN_TYPE = ((0, "Shared"), (1, "Private"))
CREW_OPTION = ((0, "Passenger Only"), (1, "Prepared to Crew"))
SAILING_EXPERIENCE = ((0, "None"), (1, "Some"), (2, "Lots"))


class Route(models.Model):
    route_name = models.CharField('Route Name', max_length=200, null=False, blank=False)
    description = models.TextField('Description', null=False, blank=False)
    duration = models.IntegerField('Duration (days)', null=False, blank=False)
    distance = models.IntegerField('Distance (miles)', null=False, blank=False)
    featured_image = CloudinaryField('Image', default='placeholder')

    class Meta:
        ordering = ['route_name']

    def __str__(self):
        return self.route_name


class Passenger(models.Model):
    first_name = models.CharField('First Name', max_length=80, null=False, blank=False)
    last_name = models.CharField('Last Name', max_length=80,null=False, blank=False)
    email = models.EmailField('Email', max_length=200, blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Trip(models.Model):
    trip_name = models.CharField('Trip Name', max_length=200, blank=False)
    trip_date = models.DateField('Trip Date')
    route_name = models.ForeignKey(Route, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(null=False, blank=False)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, blank=True, null=True)
    number_passengers = models.IntegerField('Number of Passengers')
    cabin_type = models.IntegerField('Cabin Type', choices=CABIN_TYPE, default=0)
    crew_option = models.IntegerField('Option to Crew', choices=CREW_OPTION, default=0)
    sailing_exp = models.IntegerField('Previous Sailing Experience', choices=SAILING_EXPERIENCE, default=0)
    featured_image = CloudinaryField('Image', default='placeholder')
    interest = models.ManyToManyField(Passenger, related_name='trip_interest', blank=True)

    class Meta:
        ordering = ['trip_date']

    def __str__(self):
        return self.trip_name

    def expressions_of_interest(self):
        return self.interest.count()
