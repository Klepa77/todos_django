from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.TextField()
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True)

    def get_deadline(self):
        return self.deadline.strftime('%d.%m.%y %H:%M')

    def __str__(self):
        return (f"{self.text}-"
                f"{'Завершено' if self.is_completed else 'Не завершено'}")

