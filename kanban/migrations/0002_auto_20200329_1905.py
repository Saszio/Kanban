# Generated by Django 3.0.3 on 2020-03-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dane',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
