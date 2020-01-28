from django.db import models
from django.urls import reverse
# Create your models here.

class Marks(models.Model):
    schoolboys = models.IntegerField('Школьник', default=0)
    lesson = models.IntegerField('Предмет', default=0)
    mark = models.IntegerField('Оценка', default=0)
    index = models.IntegerField('Индекс', default=0)
    date_receiv = models.DateField('Дата получения')
    date_input = models.DateTimeField() # null=True, default=True
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name