from django.db import models

# Create your models here.

class BaseDetail(models.Model):
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    email3 = models.EmailField(blank=True)
    email4 = models.EmailField(blank=True)
    email5 = models.EmailField(blank=True)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, blank=True)
    location = models.TextField()

class Homepage(models.Model):
    about = models.TextField()

class Team(models.Model):
    TEAM_CHOICES = [
        ('Board Of Directors', 'Board Of Directors'),
        ('Management', 'Management'),
    ]
    type = models.CharField(max_length=100, choices=TEAM_CHOICES)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    about = models.TextField()
    # experience = models.TextField()

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    about = models.TextField()

class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('Current Project', 'Current Project'),
        ('Completed', 'Completed'),
    ]
    type = models.CharField(max_length=100, choices=PROJECT_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    client = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.type})"

class JobOpening(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField()
    experience = models.TextField()
    location = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({'Open' if self.status else 'Closed'})"

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Us Entry from {self.name} on {self.created_at}"