from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    initials = models.CharField(max_length=2)
    email = models.EmailField()
    phone = models.DecimalField(decimal_places=0, max_digits=13)
    circle_color = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.name} {self.lastname}'


class Subtask(models.Model):
    task = models.TextField(max_length=500)
    task_state = models.BooleanField(default=False)

    def __str__(self):
        return self.task


class Tasks(models.Model):
    PRIO_CHOICES = {
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    }
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    duedate = models.DateField()
    created = models.DateField(auto_now_add=True)
    priority = models.CharField(
        max_length=6, choices=PRIO_CHOICES, default='low')
    await_feedback = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    assigned = models.ManyToManyField(Contacts, related_name='contacts')
    subtasks = models.ManyToManyField(Subtask, related_name='subtasks', blank=True)
    

    def __str__(self):
        return self.category


class Summary(models.Model):
    pass
