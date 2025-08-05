from django.db import models
from django.contrib.auth.models import User



class Event(models.Model):
    title = models.CharField(max_length=200)
    descriptions= models.TextField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'created_events')
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name = 'joined_events', blank = True)

def __str__(self):
 return self.title

class Registration(models.Model):
   event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name = 'registrations')
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   registered_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      unique_together = ('event', 'user')
   def __str__(self):
      return f'{self.user.username} registered for {self.event.title}'