from django.db import models

# Create your models here.
from django.db import models



# Create your models here.
class Books(models.Model):

    name = models.CharField(max_length=20)
    Phone_number = models.CharField(max_length=20)




    def __str__(self):
        return self.name