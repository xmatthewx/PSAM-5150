# -*- coding: UTF-8 -*-
from django import forms

from census.models import CensusInfo


class CensusFork(forms.ModelForm):

    class Meta:
        model = CensusInfo
        fields = ['name', 'email', 'street_address',  'city',  'state',  'zipcode',  'gender']
        
        