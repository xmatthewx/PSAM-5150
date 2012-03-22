# -*- coding: UTF-8 -*-
from django.contrib import admin
#from signupform.models import HelloWorld, HelloContact, Signup, Contact
from census.models import CensusInfo


class CensusAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('email', 'created_on', 'is_accepted')
    list_filter = ('is_accepted',)
    list_display_links = ('email',)
    search_fields = ['email', 'name', 'admin_comments', 'subject', ]

admin.site.register(CensusInfo, CensusAdmin)

