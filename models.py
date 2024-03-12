from django.db import models

# Create your models here.
class applicationdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Title = models.CharField(max_length=50, null=True, blank=True)
    Company = models.CharField(max_length=50, null=True, blank=True)
    Website = models.CharField(max_length=50, null=True, blank=True)
    File = models.CharField(max_length=50, null=True, blank=True)
    Coverletter = models.CharField(max_length=50, null=True, blank=True)

class contactdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Message = models.CharField(max_length=50, null=True, blank=True)

class jobpostdb(models.Model):
    Title = models.CharField(max_length=50, null=True, blank=True)
    Location = models.CharField(max_length=50, null=True, blank=True)
    Type = models.CharField(max_length=50, null=True, blank=True)
    JDescription = models.CharField(max_length=50, null=True, blank=True)
    Responsibility = models.CharField(max_length=50, null=True, blank=True)
    Qualification = models.CharField(max_length=50, null=True, blank=True)
    Salary = models.CharField(max_length=50, null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Tagline = models.CharField(max_length=50, null=True, blank=True)
    CDescription = models.CharField(max_length=50, null=True, blank=True)
    Project = models.CharField(max_length=50, null=True, blank=True)
    Website = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Number = models.IntegerField(null=True, blank=True)
    Username = models.CharField(max_length=50, null=True, blank=True)
    Logo = models.ImageField(upload_to="Profile", null=True, blank=True)

class signindb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Username = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    CPassword = models.CharField(max_length=50, null=True, blank=True)




