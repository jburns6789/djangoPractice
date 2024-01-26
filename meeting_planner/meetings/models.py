from django.db import models
from datetime import time


# Create your models here, Always need to inherit from the base class

class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} at {self.floor_number} on {self.room_number}"


class Meeting(models.Model):  # django will create the init method and db tables
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))  # start time default is 9
    duration = models.IntegerField(default=1)  # 1hour default time

    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             default=1)  # FK relation between room and meeting, can have FK w/o delete function

    # There are not allowed to be any empty fields with django

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
