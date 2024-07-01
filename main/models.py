from django.db import models


class NavbarItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name