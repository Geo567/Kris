# Generated by Django 3.0 on 2020-01-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolboys', models.IntegerField(default=0, verbose_name='Школьник')),
                ('lesson', models.IntegerField(default=0, verbose_name='Предмет')),
                ('mark', models.IntegerField(default=0, verbose_name='Оценка')),
                ('index', models.IntegerField(default=0, verbose_name='Индекс')),
                ('date_receiv', models.DateField(verbose_name='Дата получения')),
                ('date_input', models.DateTimeField()),
            ],
        ),
    ]