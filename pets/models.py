from django.db import models
from django.conf import settings
from django.utils import timezone

import uuid
import math
import os.path


def path(_,filename):
    _, extension = os.path.splitext(filename)
    return 'pets/{}{}'.format(uuid.uuid4(),extension)

class Pet(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    photo = models.ImageField(upload_to=path)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='pets',on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_on']
        
    def time_ago(self):
        now = timezone.now()
        diff=now-self.created_on
        days=diff.days
        seconds=diff.seconds

        if days == 0:
            if 0 <= seconds < 60:
                return 'just now'

            if  60 <= seconds < 3600:
                minutes=math.floor(seconds/60)
                if minutes == 1:
                    return str(minutes) + " min ago"
                return str(minutes) + " mins ago"

            if 3600 <= seconds < 86400:
                hours= math.floor(seconds/3600)
                if hours == 1:
                    return str(hours) + " hr ago"
                return str(hours) + " hrs ago"

        if 1 <= days < 30:
            if days == 1:
                return str(days) + " dy ago"
            return str(days) + " dys ago"

        if 30 <= days < 365:
            months= math.floor(days/30)
            if months == 1:
                return str(months) + " mon ago"
            return str(months) + " mons ago"

        if days >= 365:
            years= math.floor(days/365)
            if years == 1:
                return str(years) + " yr ago"
            return str(years) + " yrs ago"

class AdoptionRequest(models.Model):
    potintialOwner=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='requests',on_delete=models.CASCADE)
    pet=models.ForeignKey(Pet,related_name='requests',on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.potintialOwner} is requesting to adopt {self.pet}'