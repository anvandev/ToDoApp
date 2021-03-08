from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=180)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.name} | {self.completed} | {self.author}'
