from django.db import models

# Create your models here.
class Marks(models.Model):
    usere = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey('Lessons', on_delete=models.SET_NULL, null=True)
    mark = models.IntegerField('Оценка', default=0)
    index = models.IntegerField('Индекс', default=0)
    date_receiv = models.DateField('Дата получения')
    date_input = models.DateTimeField() # null=True, default=True
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name