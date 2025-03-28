# Generated by Django 5.1.3 on 2024-11-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0005_alter_tasks_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')], default='low', max_length=6),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='subtasks',
            field=models.ManyToManyField(blank=True, related_name='subtasks', to='backend_app.subtask'),
        ),
    ]
