# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from masterdata.models import Movie,Donor
# Register your models here.
admin.site.register(Movie)
admin.site.register(Donor)