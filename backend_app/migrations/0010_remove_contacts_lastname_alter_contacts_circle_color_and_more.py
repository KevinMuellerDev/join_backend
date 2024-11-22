# Generated by Django 5.1.3 on 2024-11-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0009_alter_tasks_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='contacts',
            name='circle_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=13, null=True),
        ),
    ]
