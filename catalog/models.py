from django.db import models
from django.urls import reverse
from django import forms

class ProfileDetails(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    Id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=70)
    Birth_Date = models.DateField()
    Gender_choices = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other')]
    Gender = models.CharField(max_length=15,choices=Gender_choices,default='i')

    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=10)
    Locality = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zip = models.IntegerField(max_length=6)
    Country = models.CharField(max_length=50)
    Service_Choices = [
    'Pharmacies',
    'Clinics',
    'Grocery Stores',
    'ATMs/Banks',
    'Restaurants',
    'PGs',
    'Hotels',
    'Police Stations',
    'Fire Stations',
    'Libraries']
    Services = forms.MultipleChoiceField(
            widget = forms.CheckboxSelectMultiple,
            choices = Service_Choices,
    )
    Profile_Pic = models.ImageField(upload_to='profile_pics', blank=True)

    #add forms
    class Meta:
        ordering = ['Id', 'Name', 'Birth_Date']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('user-detail', args=[str(self.Id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.Id}: {self.Name}'

# now the forms class for mutliple choice

