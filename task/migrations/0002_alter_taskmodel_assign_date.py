# Generated by Django 5.0 on 2023-12-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='assign_date',
            field=models.DateTimeField(),
        ),
    ]
