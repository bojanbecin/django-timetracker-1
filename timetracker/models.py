from django.db import models
from django.utils import timezone

class Employee(models.Model):
    firstName = models.CharField(max_length = 64)
    lastName = models.CharField(max_length = 64)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Project(models.Model):
    name = models.CharField(max_length = 256)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __str__(self):
        return self.name

class WorkSegment(models.Model):
    date = models.DateTimeField()
    employee = models.ForeignKey(Employee)
    project = models.ForeignKey(Project)
    numHours = models.IntegerField()

    def weekNum(self):
        return self.date.isocalendar()[1]

    def __str__(self):
        return str(self.date) + ' ' + str(self.employee) + ' ' + str(self.project) + ' ' + str(self.numHours)
