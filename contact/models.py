from django.db import models

# Create your models here.

class Contact (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=320)
    phone=models.PositiveIntegerField()
    message=models.CharField(max_length=600)

    def __str__(self):
        texto = "Name: {0} Email: {1} Phone: {2} Message: {3}"        
        return texto.format(self.name, self.email, self.phone, self.message)