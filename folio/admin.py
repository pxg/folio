# -*- coding: utf-8 -*-
from django.contrib import admin
# from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminBase
# from django.contrib.flatpages.models import FlatPage
#from orderedmodel import OrderedModelAdmin
from folio.models import Project

admin.site.register(Project)