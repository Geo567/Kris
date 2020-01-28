from django.db import models
from django.urls import reverse

class Article(models.Model):
    name = models.CharField('Имя', max_length=120)
    mail = models.EmailField('E-mail', default=0)
    school = models.IntegerField('Школа', default=0)
    level = models.IntegerField('Класс', default=0)
    password = models.CharField('Пароль',max_length=50 )
    fiscul = models.BooleanField('Физ-ра', default=False)
    lit = models.BooleanField('Литература', default=False)
    algebra = models.BooleanField('Алгебра', default=False)
    geomet = models.BooleanField('Геометрия', default=False)
    history = models.BooleanField('История', default=False)
    fiscul_t = models.FloatField('Физ-ра--цель', null=True, blank=True, default=None)
    lit_t = models.FloatField('Литература--цель', null=True, blank=True, default=None)
    algebra_t = models.FloatField('Алгебра--цель',null=True, blank=True, default=None)
    geomet_t = models.FloatField('Геометрия--цель',null=True, blank=True, default=None)
    history_t = models.FloatField('История--цель',null=True, blank=True, default=None)
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
