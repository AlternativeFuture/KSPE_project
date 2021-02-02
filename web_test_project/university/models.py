from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=250, null=True)  # , validators=
