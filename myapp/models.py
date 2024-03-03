from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(null=True)

    def __str__(self):
        return f"{self.destination.name} on {self.date.strftime('%Y-%m-%d')}"
