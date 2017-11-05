from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)
    first_review_date = models.DateTimeField('date first reviewed')
    last_review_date = models.DateTimeField('date last reviewed')
    permanently_closed = models.IntegerField(default=0) 
    def __str__(self):
        return self.name
