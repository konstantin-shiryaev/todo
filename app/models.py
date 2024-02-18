from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=255)
    is_done = models.BooleanField()

    def __str__(self):
        return f"{'Выполнено' if self.is_done else f'Не выполнено'} - {self.text}"

class Person(models.Model):
    user_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.user_name} {self.last_name}, {self.age} лет"

