# -*- coding: UTF-8 -*-
from django.contrib import admin
from census.models import CensusInfo


class CensusAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('name', 'created_on', 'is_accepted')
    list_filter = ('is_accepted','state')
    list_display_links = ('name',)
    search_fields = ['email', 'name', 'admin_comments', 'state', 'city' ]

admin.site.register(CensusInfo, CensusAdmin)

