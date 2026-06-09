from datetime import datetime
import email
from urllib import request

from django.db import models
import bcrypt

class UserManager(models.Manager):
    def create_user(self, data):
        hashed_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode()
        user = self.create(username=data['username'], email=data['email'], password=hashed_password)
        return user
    
    def authenticate(self, email, password):
        errors = {}
        user = self.filter(email=email).first()

        if user:
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return errors, user
            else:
                errors['login'] = "Invalid email or password."
        else:
            errors['login'] = "Invalid email or password."

        return errors, None
    
    def validate_registration(self, data):
        errors = {}
        birthday_obj = None

        if not data.get('birthday'):
            errors['birthday'] = "Birthday is required."
        else:
            try:
                birthday_obj = datetime.strptime(data['birthday'], '%Y-%m-%d').date()
            except ValueError:
                errors['birthday'] = "Invalid birthday format."

        if len(data.get('username', '')) < 3:
            errors['username'] = "Username must be at least 3 characters long."
        if not data.get('email') or '@' not in data['email']:
            errors['email'] = "Invalid email address."
        if len(data.get('password', '')) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        if data.get('password') != data.get('confirm_password'):
            errors['confirm_password'] = "Passwords do not match."
        if data.get('email') and self.filter(email=data['email']).exists():
            errors['email'] = "Email is already registered."

        if birthday_obj:
            if birthday_obj > datetime.today().date():
                errors['birthday'] = "Birthday cannot be in the future."
            else:
                age = (datetime.today().date() - birthday_obj).days // 365
                if age < 13:
                    errors['birthday'] = "You must be at least 13 years old."

        return errors
    

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    objects = UserManager()
    def __str__(self):
        return self.username
