# Generated by Django 4.2 on 2023-04-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
