from django.db import models

class Room(models.Model):
    block = models.CharField(max_length=10)
    room_number = models.CharField(max_length=10)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.block} - {self.room_number}"


class Feedback(models.Model):
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
