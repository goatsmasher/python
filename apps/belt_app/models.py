from __future__ import unicode_literals
from ..main_app.models import Register
from django.db import models
import datetime

# Create your models here.


class AppointmentManager(models.Manager):
    def add_appt(self, postData, id):
        errors = []
        if self.filter(task=postData['task']):
            errors.append('Task already exists!')
        if self.filter(time=postData['time']).filter(date=postData['date']):
            errors.append('A task already exists for this time!')
            
        response = {}
        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            self.create(task = postData['task'], status = "Pending", user = Register.objects.get(id=id), date = postData['date'], time = postData['time'])
        return response

    def edit_appt(self, postData, id):
        appointment = self.get(id=id)
        errors = []
        if self.filter(task=postData['task']):
            errors.append('Task already assigned')
        if postData['task']:
            appointment.task = postData['task']
        if postData['status']:
            appointment.status = postData['status']
        if postData['date']:
            appointment.date = postData['date']
        if postData['time']:
            appointment.time = postData['time']
        appointment.save()


class Appointment(models.Model):
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(Register, related_name = "user_appt")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AppointmentManager()