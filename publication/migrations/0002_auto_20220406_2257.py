# Generated by Django 3.2.5 on 2022-04-07 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='author',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='content2',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='content3',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
