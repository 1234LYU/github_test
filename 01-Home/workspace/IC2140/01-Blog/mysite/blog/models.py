from django.db import models

# Create your models here.
class Entry(models.Model):
#Fields
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
#Methods
    def __str__(self):
        return 'Entry #{}'.format(self.id)
    class Meta:
        verbose_name_plural = 'entries'

class Inventory(models.Model):
#Fields
    Inventory_no = models.TextField()
    Location = models.TextField()
    Owner = models.TextField()
    Description = models.TextField()
    Price = models.TextField()
    Purchase_Date = models.TextField()
    Active = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
#Methods
    def __str__(self):
        return 'Inventory #{}'.format(self.id)
    class Meta:
        verbose_name_plural = 'Inventories'

class Owner(models.Model):
#Fields
    Owner = models.TextField()
    Full_Name = models.TextField()
    Title = models.TextField()
    Phone = models.TextField()
    Email = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
#Methods
    def __str__(self):
        return 'Owner #{}'.format(self.id)
    class Meta:
        verbose_name_plural = 'Owners'
