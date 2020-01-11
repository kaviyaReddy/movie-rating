# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    ratings = models.CharField(max_length=10,blank=True, null=True)

    def __str__(self):
        return self.name

class Donor(models.Model):
	first_name=models.CharField(max_length=20,blank=True,null=True)
	middle_name=models.CharField(max_length=20,blank=True,null=True)
	last_name=models.CharField(max_length=20,blank=True,null=True)
	amount=models.CharField(max_length=100,blank=True,null=True)

	def __str__(self):
 		return self.first_name
