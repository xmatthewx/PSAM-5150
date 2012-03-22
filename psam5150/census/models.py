from django.db import models

# Create your models here.


STATE_CHOICES = (
('AL', 'Alabama'),
('AK', 'Alaska'),
('AZ', 'Arizona'),
('AR', 'Arkansas'),
('CA', 'California'),
('CO', 'Colorado'),
('CT', 'Connecticut'),
('DE', 'Delaware'),
('FL', 'Florida'),
('GA', 'Georgia'),
('HI', 'Hawaii'),
('ID', 'Idaho'),
('IL', 'Illinois'),
('IN', 'Indiana'),
('IA', 'Iowa'),
('KS', 'Kansas'),
('KY', 'Kentucky'),
('LA', 'Louisiana'),
('ME', 'Maine'),
('MD', 'Maryland'),
('MA', 'Massachusetts'),
('MI', 'Michigan'),
('MN', 'Minnesota'),
('MS', 'Mississippi'),
('MO', 'Missouri'),
('MT', 'Montana'),
('NE', 'Nebraska'),
('NV', 'Nevada'),
('NH', 'New Hampshire'),
('NJ', 'New Jersey'),
('NM', 'New Mexico'),
('NY', 'New York'),
('NC', 'North Carolina'),
('ND', 'North Dakota'),
('OH', 'Ohio'),
('OK', 'Oklahoma'),
('OR', 'Oregon'),
('PA', 'Pennsylvania'),
('RI', 'Rhode Island'),
('SC', 'South Carolina'),
('SD', 'South Dakota'),
('TN', 'Tennessee'),
('TX', 'Texas'),
('UT', 'Utah'),
('VT', 'Vermont'),
('VA', 'Virginia'),
('WA', 'Washington'),
('WV', 'West Virginia'),
('WI', 'Wisconsin'),
('WY', 'Wyoming'),
)


GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('T', 'Trans'),
    ('O', 'Other'),
)

class CensusInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    #country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_accepted = models.BooleanField(default=False)
    admin_comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField()

    def __unicode__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey('country', related_name='state')
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey('country', related_name='cities')
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class House(models.Model):
    city = models.ManyToManyField('City', related_name='houses')
    street = models.CharField(max_length=300)

    def __unicode__(self):
        return self.street