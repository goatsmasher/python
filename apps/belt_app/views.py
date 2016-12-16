from django.shortcuts import render, redirect
from .models import Wishlist
from ..main_app.models import Register
# Create your views here.

def index(request):
    try:
        request.session['response']
    except:
        return redirect('/')
    context = {
        "wishes" : Wishlist.objects.all().exclude(user=request.session['id']),
        "username" : Register.objects.all(),
        "wishlist" : Wishlist.objects.filter(user=request.session['id']).filter(user__id=request.session['id']),
    }
    return render(request, 'belt_app/index.html', context)

def create(request):
    if request.method == "POST":
        Wishlist.objects.add_item(request.POST, request.session['id'])
        return redirect('belt:index')
    return render(request, 'belt_app/add_item.html')

def destroy(request, id):
    item_to_delete = Wishlist.objects.get(id=id)
    item_to_delete.delete()
    return redirect('belt:index')

def add_wish(request, id):
    add_wish = Wishlist.objects.get(id=id)
    Wishlist.objects.add_wish(add_wish.id, request.session['id'])
    return redirect('belt:index')

def del_wish(request, id):
    Wishlist.objects.del_wish(id, request.session['id'])

    return redirect('belt:index')

def show(request, id):
    show_item = Wishlist.objects.get(id=id)
    user = Wishlist.objects.filter
    context = {
        "item" : show_item,
    }
    return render(request, 'belt_app/item_show.html', context)