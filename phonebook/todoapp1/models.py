from django.db import models

# Create your models here.



class todo(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the name")
    date_time = models.DateTimeField(null=True,blank=True, help_text="Select date and time")
    is_true = models.BooleanField(default=False, help_text="Select True or False")

    def __str__(self):
        return self.name