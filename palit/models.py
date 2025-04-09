from django.db import models

class ColorScheme(models.Model):
    name = models.CharField(max_length=100, unique=True)
    background = models.CharField(max_length=20)
    menu = models.CharField(max_length=20)
    menu_text = models.CharField(max_length=20)
    text = models.CharField(max_length=20)
    header = models.CharField(max_length=20, default='#222222')
    sidebar = models.CharField(max_length=20, default='#3a4f59')
    card = models.CharField(max_length=20, default='#ffffff')
    footer = models.CharField(max_length=20, default='#444444')

    def __str__(self):
        return self.name