from django.db import models

# Follow the GUIDE [https://medium.com/@codewithbushra/using-sqlite-as-a-database-backend-in-django-projects-code-with-bushra-d23e3100686e]

# First Create a new Project so it doesn't conflict with the existing one
# django-admin startproject eventSystem

# Then create a new app inside the project
# python manage.py startapp eventManageSystem

# Then, add the new app to your project's settings.py file
# INSTALLED_APPS = [
#     ...
#     'eventManageSystem',
# ]

# FOLLOW THE GUIDE TO CREATE THE MODELS
# CREATE A SUPERUSER TO ACCESS THE ADMIN PANEL
# python manage.py createsuperuser

# FOR A MORE COMFORTABLE VIEWING OF THE TABLES, USE DB BROWSER FOR SQLITE
# https://sqlitebrowser.org/dl/

# Create your models here.
class Organizer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.first_name
    
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True) # According to Guide, auto_now_add=True is for defaulting to current time on creation
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending') # Don't know how the choices work, so I just copied from Guide

    def __str__(self):
        return f"Registration of {self.participant} for {self.event} - {self.status}"