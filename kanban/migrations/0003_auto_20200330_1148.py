# Generated by Django 3.0.4 on 2020-03-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_auto_20200329_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dane',
            name='status',
            field=models.IntegerField(),
        ),
    ]
