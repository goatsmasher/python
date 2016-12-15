from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import re
import bcrypt
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class RegisterManager(models.Manager):
    def register(self, postData):
        errors = []
        if self.filter(email=postData['email']):
            errors.append('Email already in use')
        if len(postData['first_name']) < 2:
            errors.append('First name must be longer than two letters')
        if len(postData['last_name']) < 2:
            errors.append('Last name must be longer than two letters')
        if not NAME_REGEX.match(postData['first_name']):
            errors.append('Your first name must contain only letters')
        if not NAME_REGEX.match(postData['last_name']):
            errors.append('Your last name must contain only letters')
        if postData['password'] != postData['confirm_password']:
            errors.append('Your passwords do not match')
        password = postData['password'].encode('utf-8')
        pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())

        response = {}
        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = pw_hash)
        return response


    def login(self, request):
        user = self.filter(email=request.POST['email'])
        if not user:
            return (False, "Email/Password doesn't match.")
        else:
            password = request.POST['password'].encode()
            if self.filter(password = bcrypt.hashpw(password, user[0].password.encode())):
                user = self.get(email=request.POST['email'])
                return (True, user)
            else:
                return (False, "Email/Password doesn't match.")

class Register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    objects = RegisterManager()