from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    # unique key to distinguish between different url
    slug = models.SlugField(max_length=250,
                            unique_for_date='created')
    # address of event
    venue = models.CharField(max_length=250)
    event_fee = models.IntegerField()
    description = models.CharField(max_length=1000, blank=True)
    event_time = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('eventsapp:event_detail',
                       args=[self.created.year,
                             self.created.strftime('%m'),
                             self.created.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ('-created',)
        # sort post by created field

    def __str__(self):
        return self.title


class Profile(models.Model):
    SEX_CHOICES = (('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER'))
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    sex = models.CharField(choices=SEX_CHOICES, default='male', max_length=10, blank=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering = ('-created', )


class Ticket(models.Model):
    # store each attend with a ticket to that event
    user = models.ForeignKey(Profile)
    event = models.ForeignKey(Event)
    total_tickets = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.event.event_fee * self.total_tickets

    def __str__(self):
        return self.event.title

    class Meta:
        ordering = ('-created', )
        unique_together = ('user', 'event')