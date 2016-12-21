from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register, RegisterManager


# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def register(request):
    response = Register.objects.register(request.POST)
    if not response['status']:
        for error in response['errors']:
            messages.error(request, error)
            return redirect('/')
    request.session['response'] = {
        'activity' : "Registered",
        'name' : request.POST['name'],
    }
    user_id = Register.objects.get(name=request.POST['name'])
    request.session['id'] = user_id.id
    return redirect('/success')

def login(request):
    try:
        response = Register.objects.login(request)
        if response[0] == False:
            messages.error(request, response[1])
            return redirect('/')
    except:
        return redirect('/')
    return log_in(request, response[1])

def log_in(request, response):
    request.session['response'] = {
        'activity' : "Logged In",
        'name' : response.name,
    }
    request.session['id'] = response.id
    print request.session['id']
    return redirect('/success')

def logout(request):
    try:
        del request.session['response']
    except:
        pass
    return redirect('/')

def success(request):
    try:
        request.session['response']
    except:
        return redirect('/')
    return render(request, 'main_app/success.html')