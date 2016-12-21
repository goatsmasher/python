from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from ..main_app.models import Register
from django.contrib import messages
import datetime
from datetime import date
# Create your views here.

def index(request):
    context = {
        "today" : date.today(),
        "todays_appt" : Appointment.objects.filter(date=date.today()).filter(user=request.session['id']).order_by('time'),
        "upcoming" : Appointment.objects.all().exclude(date=date.today()).filter(user=request.session['id']).order_by('time').order_by('date'),
    }
    return render(request, 'belt_app/index.html', context)

def add_appt(request):
    response = Appointment.objects.add_appt(request.POST, request.session['id']),
    print response
    if response[0] == False:
        context = {
            "message" : "Appointment Creation Failed"
        }
        messages.error(request, response[1])
        return redirect('belt:index')
    return redirect('belt:index')
    

def edit(request, id):
    if request.method == "POST":
        Appointment.objects.edit_appt(request.POST, id)
        return redirect('belt:index')

def edit_page(request, id):
    show_item = Appointment.objects.get(id=id)
    show_date = show_item.date.strftime('%m-%d-%Y')
    context = {
        "editing" : show_item,
        "date" : show_date
    }
    print show_date
    return render(request, 'belt_app/edit_page.html', context)

def destroy(request, id):
    item_to_delete = Appointment.objects.get(id=id)
    item_to_delete.delete()
    return redirect('belt:index')
