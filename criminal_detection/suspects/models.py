from django.db import models

class Suspect(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    crime_incidents = models.TextField()
    arrest_reason = models.TextField()
    photo = models.ImageField(upload_to='suspect_photos/')
    # Add other fields as needed

    def __str__(self):
        return self.name
