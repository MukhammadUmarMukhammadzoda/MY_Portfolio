import email
from statistics import mode
from tkinter import TRUE
from django.db import models

# Create your models here.
class Skill(models.Model):
    skill = models.CharField(max_length=50, null=True, blank=True)
    percent = models.IntegerField(null=True)


    def __str__(self):
        return self.skill




class Service(models.Model):
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


class Experience(models.Model):
    name = models.CharField(max_length=40, null=True)
    additional_info = models.CharField(max_length=50, blank=True, null=True)
    started_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return self.name

   
class Project(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.name


class Client(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name