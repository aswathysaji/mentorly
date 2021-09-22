from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField('Full Name',max_length=50)
    email = models.EmailField('Email')
    skills = models.TextField('Skills')
    description = models.TextField('Description')
    experience = models.TextField('Experience')
    calendly = models.URLField('Calendly',default='')

    def __str__(self):
        return self.name
