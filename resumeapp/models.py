from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    emailid = models.CharField(max_length=100)
    phoneno = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    dob = models.DateField()
    technicalskills = models.CharField(max_length=100)
    projects = models.TextField()
    internship = models.CharField(max_length=300)
    schoolname = models.CharField(max_length=50, default="ABC")
    schoolqualification = models.CharField(max_length=50)
    schoolduration = models.IntegerField()
    collegename = models.CharField(max_length=50, default="ABC")
    collegequalification = models.CharField(max_length=50)
    collegeduration = models.IntegerField()
    graduatedcollegename = models.CharField(max_length=50, default="ABC")
    graduatequalification = models.CharField(max_length=50)
    graduateduration = models.IntegerField()
    hobbies = models.CharField(max_length=300)
    languagesknown = models.CharField(max_length=100)
    nationality = models.CharField(max_length=30)
    certification = models.TextField()
    state = models.CharField(max_length=100)
    maritalstatus = models.CharField(max_length=40)
    summary = models.TextField()
