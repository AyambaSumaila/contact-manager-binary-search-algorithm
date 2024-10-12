from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    group = models.CharField(max_length=100, blank=True, null=True)
    favorite = models.BooleanField(default=False)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
