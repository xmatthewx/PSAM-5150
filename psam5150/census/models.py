from django.db import models

# Create your models here.


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
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_accepted = models.BooleanField(default=False)
    admin_comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name
