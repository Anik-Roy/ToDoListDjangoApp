from django.db import models

# Create your models here.
class ToDo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.text == '':
            raise ValidationError('Empty error message')