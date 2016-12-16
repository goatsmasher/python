from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import re
import bcrypt
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class RegisterManager(models.Manager):
    def register(self, postData):
        errors = []
        if self.filter(username=postData['username']):
            errors.append('Username already in use')
        if len(postData['name']) < 3:
            errors.append('Name must be longer than three letters')
        if len(postData['username']) < 3:
            errors.append('Username must be longer than two letters')
        if not NAME_REGEX.match(postData['name']):
            errors.append('Your Name must contain only letters')
        if postData['password'] != postData['confirm_password']:
            errors.append('Your passwords do not match')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters') 
        password = postData['password'].encode('utf-8')
        pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        response = {}
        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            self.create(name = postData['name'], username = postData['username'], password = pw_hash, datehired = postData['datehired'])
            # request.session['id'] = Register.objects.get(username=postData['username'])
        return response


    def login(self, request):
        user = self.filter(username=request.POST['username'])
        if not user:
            return (False, "Username/Password doesn't match.")
        else:
            password = request.POST['password'].encode()
            if self.filter(password = bcrypt.hashpw(password, user[0].password.encode())):
                user = self.get(username=request.POST['username'])
                return (True, user)
            else:
                return (False, "Username/Password doesn't match.")

class Register(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    datehired = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    objects = RegisterManager()