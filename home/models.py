from django.db import models
from django.core.validators import RegexValidator



class Projects(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(default=None)
    employee = models.CharField(max_length=100, blank=True, null=True)
    employee2 = models.CharField(max_length=100, blank=True, null=True)
    img = models.FileField(upload_to='images', blank=True, null=True)
    employee_img = models.FileField(upload_to='images', blank=True, null=True, default=None)
    employee2_img = models.FileField(upload_to='images', blank=True, null=True, default=None)
    employee_url = models.URLField(max_length=200, blank=True, null=True, default=None)
    employee2_url = models.URLField(max_length=200, blank=True, null=True, default=None)
    project_url = models.URLField(max_length=500, blank=True, null=True, default=None)
    
    
class Messages(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?98?\d{9,15}$', message="Example: +9121234567")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    message = models.TextField(blank=False)
    
    