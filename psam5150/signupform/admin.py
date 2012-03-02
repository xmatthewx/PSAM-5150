# -*- coding: UTF-8 -*-
from django.contrib import admin
#from signupform.models import HelloWorld, HelloContact, Signup, Contact
from signupform.models import HelloWorld, Signup, Contact

class HelloWorldAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('created_on', 'name', 'location', )

#class HelloContactAdmin(admin.ModelAdmin):
#    date_hierarchy = 'created_on'
#    list_display = ('created_on', 'name', 'city', )




class SignupAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('email', 'created_on', 'is_accepted', 'url',)
    list_filter = ('is_accepted',)
    list_display_links = ('email',)
    search_fields = ['email', 'name', 'admin_comments', 'url','reason_for_joining', ]

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('email', 'created_on', 'is_accepted')
    list_filter = ('is_accepted',)
    list_display_links = ('email',)
    search_fields = ['email', 'name', 'admin_comments', 'subject', ]

admin.site.register(HelloWorld, HelloWorldAdmin)
#admin.site.register(HelloContact, HelloContactAdmin)
admin.site.register(Signup, SignupAdmin)
admin.site.register(Contact, ContactAdmin)

