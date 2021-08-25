from django.db import models
from django.contrib.auth.models import User


class Applicant(models.Model):

    QUALIFICATION = (
                    ('Under Graduate', 'Under Graduate'),
                    ('Graduate', 'Graduate'),
                    ('Post Graduate', 'Post Graduate')
    )

    EXPERIANCE = (
        ('Fresher', 'Fresher'),
        ('1-3', '1-3'),
        ('4-6', '4-6'),
        ('6-10', '6-10'),
        ('More than 10', 'More than 10')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.IntegerField(null=True)
    address = models.TextField(null=True)
    qualification = models.CharField(
        max_length=250, null=True, choices=QUALIFICATION)
    experiance = models.CharField(
        max_length=250, null=True, choices=EXPERIANCE)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Companies(models.Model):

    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.IntegerField(null=True)
    address = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Jobs(models.Model):

    QUALIFICATION = (
                    ('Under Graduate', 'Under Graduate'),
                    ('Graduate', 'Graduate'),
                    ('Post Graduate', 'Post Graduate')
    )

    EXPERIANCE = (
        ('Fresher', 'Fresher'),
        ('1-3', '1-3'),
        ('4-6', '4-6'),
        ('6-10', '6-10'),
        ('More than 10', 'More than 10')
    )

    companies = models.ForeignKey(
        Companies, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=True)
    qualification = models.CharField(
        max_length=250, null=True, choices=QUALIFICATION)
    experiance = models.CharField(
        max_length=250, null=True, choices=EXPERIANCE)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Application(models.Model):

    applicant = models.ForeignKey(
        Applicant, null=True, on_delete=models.CASCADE)
    jobs = models.ForeignKey(Jobs, null=True, on_delete=models.SET_NULL)
    date_applied = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.applicant)
