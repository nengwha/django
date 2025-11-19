from django.contrib import admin
from .models import Organizer, Category, Event, Participant, Registration

admin.site.register(Organizer)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Registration)