# Generated by Django 4.2.7 on 2023-12-31 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_categorymodel_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='task',
        ),
    ]
