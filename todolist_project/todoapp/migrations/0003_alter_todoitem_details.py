# Generated by Django 5.1 on 2024-08-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todoitem_date_todoitem_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='details',
            field=models.TextField(),
        ),
    ]
