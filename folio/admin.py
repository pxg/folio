# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
#from django.contrib.flatpages.models import FlatPage
#from orderedmodel import OrderedModelAdmin
from folio.models import Project, Copy

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    # list_filter = ['asked_date', 'approved']
    # search_fields = ['question']
    # ordering = ['asked_date', 'approved']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Copy)