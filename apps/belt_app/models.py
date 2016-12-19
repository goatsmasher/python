from __future__ import unicode_literals
from ..main_app.models import Register
from django.db import models

# Create your models here.

class WishlistManager(models.Manager):
    def add_item(self, postData, id):
        self.create(item = postData['item'], created_by = Register.objects.get(id=id))
        person = Register.objects.get(id=id)
        wishlist = self.get(item = postData['item'])
        wishlist.user.add(person)

    def add_wish(self, wish_id, id):
        person = Register.objects.get(id=id)
        wishlist = self.get(id = wish_id)
        wishlist.user.add(person)
        # wishlist.created_by.add(person)

    def del_wish(self, wish_id, id):
        person = Register.objects.get(id=id)
        wishlist = self.get(id = wish_id)
        wishlist.user.remove(person)
    

        
class Wishlist(models.Model):
    item = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    user = models.ManyToManyField(Register, related_name = "wishes")
    created_by = models.ForeignKey(Register, related_name = "created_for")

    objects = WishlistManager()
