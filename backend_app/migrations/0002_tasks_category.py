# Generated by Django 5.1.3 on 2024-11-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
