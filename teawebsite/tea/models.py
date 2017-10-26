from django.db import models
from django.urls import reverse

# Create your models here.

# Preperation method model
class BrewingMethod(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the name of this brewing method.", primary_key=True)
    
    description = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.name

# Tea model
class Tea(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="Enter the name of the tea.")
    
    # save names of tea images to be used, these files will be stored in static/imgs
    image_name1 = models.CharField(max_length=100, blank=True)
    image_name2 = models.CharField(max_length=100, blank=True)
    
    description = models.TextField(max_length=500, help_text="Tea details", null=True)
    
    brewing_method = models.ManyToManyField(BrewingMethod, help_text="Select the brewing methods.")

    def __str__(self):
        return "{0}".format(self.name)
    
    # get url of specific tea
    def get_absolute_url(self):
        return reverse('tea-detail', args=[str(self.id)])
