from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save


STATUS = ((0, 'Draft'), (1, 'Published'))
CABIN_TYPE = ((0, "Shared"), (1, "Private"))
CREW_OPTION = ((0, "Passenger Only"), (1, "Prepared to Crew"))
SAILING_EXPERIENCE = ((0, "None"), (1, "Some"), (2, "Lots"))


class Route(models.Model):
    route_name = models.CharField(
        'Route Name', max_length=200, blank=False, unique=True)
    description = models.TextField('Description', blank=False)
    duration = models.IntegerField('Duration (days)', null=False, blank=False)
    distance = models.IntegerField(
        'Distance (nautical miles)', null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('Image', default='placeholder')

    class Meta:
        ordering = ['route_name']

    def __str__(self):
        return self.route_name


class Trip(models.Model):
    trip_date = models.DateField('Trip Date')
    route_name = models.ForeignKey(
        Route, on_delete=models.CASCADE, blank=False, null=True)
    description = models.TextField('Description', blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    interest = models.ManyToManyField(
        User, related_name='trip_interest', blank=True)

    class Meta:
        ordering = ['trip_date']

    def __str__(self):
        return str(self.trip_date)

    def expressions_of_interest(self):
        return self.interest.count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField('Bio', blank=True)
    sailing_exp = models.IntegerField(
        'Previous Sailing Experience', choices=SAILING_EXPERIENCE, default=0)

    # Automatically create a Profile when adding a new user
    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = Profile(user=user)
            user_profile.save()
    post_save.connect(create_profile, sender=User)

    def __str__(self):
        return str(self.user)


class Booking(models.Model):
    trip_date = models.ForeignKey(
        Trip, on_delete=models.CASCADE, blank=False, null=True)
    route_name = models.ForeignKey(
        Route, on_delete=models.CASCADE, blank=False, null=True)
    passenger = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=True)
    number_passengers = models.IntegerField('Number of Passengers')
    cabin_type = models.IntegerField(
        'Cabin Type', choices=CABIN_TYPE, default=0)
    crew_option = models.IntegerField(
        'Option to Crew', choices=CREW_OPTION, default=0)
    sailing_exp = models.IntegerField(
        'Previous Sailing Experience', choices=SAILING_EXPERIENCE, default=0)
    special_assistance = models.TextField(
        'Special Assistance Needs', blank=True)
    comments = models.TextField(
        'Any additional comments', blank=True)

    class Meta:
        ordering = ['trip_date']

    def __str__(self):
        return str(self.route_name)
