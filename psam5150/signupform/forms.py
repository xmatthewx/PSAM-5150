# -*- coding: UTF-8 -*-
from django import forms

from signupform.models import Signup
from signupform.models import Contact

class HelloWorldForm(forms.Form):
    name = forms.CharField(max_length=100)
    location = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

#class HelloContactForm(forms.Form):
#    name = forms.CharField(max_length=100)
#    city = forms.CharField(max_length=200)
#    question = forms.CharField(widget=forms.Textarea)


class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        #fields = ['name', 'email', 'reason_for_joining', 'picture', 'url']
        fields = ['name', 'email', 'reason_for_joining', 'url']


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
#       fields = ['name', 'email', 'street_address',  'city', 'state',  'zipcode' ]
        fields = ['name', 'email', 'street_address',  'city',  'state',  'zipcode',  'subject', 'question']

