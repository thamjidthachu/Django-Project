# Generated by Django 4.0.1 on 2022-01-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
