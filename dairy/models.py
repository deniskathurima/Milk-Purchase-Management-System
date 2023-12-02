from django.db import models


# Create your models here.

class Register(models.Model):
    firstName = models.CharField(max_length=100, blank=False, null=False)
    lastName = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    dateOfRegistration = models.DateTimeField(auto_now_add=True)
    mobileNumber = models.CharField(max_length=100, blank=False, null=False)

    def save(self, *args, **kwargs):
        super(Register, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class MilkRecord(models.Model):
    farmer = models.ForeignKey(Register, on_delete=models.CASCADE)
    milk_qty = models.PositiveIntegerField()
