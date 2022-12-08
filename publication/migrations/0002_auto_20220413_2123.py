# Generated by Django 3.2.5 on 2022-04-14 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='statusPublication',
        ),
        migrations.AddField(
            model_name='carousel',
            name='ordenPublication',
            field=models.CharField(blank=True, choices=[('N', 'No visible'), ('1', 'Carusel 1'), ('2', 'Carusel 2'), ('3', 'Carusel 3')], default='D', max_length=1),
        ),
    ]