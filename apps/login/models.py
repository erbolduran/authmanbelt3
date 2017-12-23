# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models


NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        # check DB for post_data['username']
        if len(self.filter(username=post_data['username'])) > 0:
            # check this user's password
            user = self.filter(username=post_data['username'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('username/password incorrect')
        else:
            errors.append('username/password incorrect')

        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []
        # check length of name fields
        if len(post_data['name']) < 2 or len(post_data['username']) < 2:
            errors.append("name fields must be at least 3 characters")
        # check length of name password
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
        # check name fields for letter characters            
        if not re.match(NAME_REGEX, post_data['name']) or not re.match(NAME_REGEX, post_data['username']):
            errors.append('name fields must be letter characters only')
        # check uniqueness of email
        if len(User.objects.filter(username=post_data['username'])) > 0:
            errors.append("username already in use")
        # check password == password_confirm
        if post_data['password'] != post_data['password_confirm']:
            errors.append("passwords do not match")


        if not errors:
            # make our new user
            # hash password
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))
            new_user = self.create(
                name=post_data['name'],
                username=post_data['username'],
                password=hashed
            )
            print new_user
            return new_user
        return errors


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)


    objects = UserManager()
    def __unicode__(self):
        return 'name: {}, username: {}, password: {}, id: {}'.format(self.name, self.username, self.password, self.id)

