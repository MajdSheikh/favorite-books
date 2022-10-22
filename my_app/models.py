from distutils.command.upload import upload
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address!"



        # if User.objects.filter(email = postData['email']).exists():
        #     errors['email'] = ("Email already exists, try logging in.")


        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if (postData["first_name"]).isalpha():
            errors["first_name"] = "First name should be letters"

        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if (postData["last_name"]).isalpha():
            errors["last_name"] = "last name should be letters"

        if len(postData["password"]) < 8:
            errors["password"] = " your password should be at least 8 characters"
        if (postData["password"]) != postData["confirm_PW"]:
            errors["confirm_PW"] = "your passwords did not match"

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_PW = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 
    # liked books
    # books uploaded


class BookManager(models.Manager):
    def basicc_validator(self, postData):
        
        errors = {}
        if len(postData["title"]) < 1:
            errors["title"] = "title must be provided"
        
        if len(postData["desc"]) < 5:
            errors["desc"] = "description must be at least 5 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    users_who_like = models.ManyToManyField(User, related_name="linked_books") #list of users who like a given book
    uploaded_by = models.ForeignKey(User, related_name= "books_uploaded", on_delete = models.CASCADE) #the user who uploaded a given book
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=BookManager()