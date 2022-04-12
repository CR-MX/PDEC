# Generated by Django 3.2.5 on 2022-04-12 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0004_alter_publication_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='section',
            field=models.CharField(blank=True, choices=[('F', 'First_Section'), ('1', 'Second_Sec_1'), ('2', 'Second_Sec_2'), ('3', 'Second_Sec_3'), ('T', 'Third_Section')], default='some_value', max_length=1),
        ),
    ]
