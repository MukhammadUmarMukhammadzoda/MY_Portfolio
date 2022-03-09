from statistics import mode
from django.db import models

# Create your models here.
class Skills(models.Model):
    skill = models.CharField(max_length=50, null=True, blank=True)
    percent = models.IntegerField(null=True)


    def __str__(self):
        return self.skill




class Services(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    name = models.CharField(max_length=40, null=True)
    additional_info = models.CharField(max_length=50, blank=True, null=True)
    started_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return self.name


class Experiences(models.Model):
    name = models.CharField(max_length=40, null=True)
    additional_info = models.CharField(max_length=50, blank=True, null=True)
    started_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return self.name

   
class Projects(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.name


class Clients(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
