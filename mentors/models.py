from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.

class Mentor(models.Model):
    name = models.CharField('Full Name',max_length=50)
    skills = models.TextField('Skills')
    calendly = models.URLField('Calendly Link',max_length=200)
    image = models.ImageField('Image',upload_to='images/')
    def __str__(self):
        return self.name
