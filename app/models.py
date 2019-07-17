from django.db import models
from .models_data import TEST_CASES_STATUSES
from django.contrib.auth.models import User


# Create your models here.
class TestCase(models.Model):
    def __str__(self):
        return self.title
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default="")
    description = models.TextField()
    preconditions = models.TextField()
    status = models.CharField(max_length=20, choices=TEST_CASES_STATUSES, default='new')
    project_id = models.ForeignKey("Project", to_field='id', on_delete=models.DO_NOTHING)
    #stab for comments


class Project(models.Model):
    def __str__(self):
        return self.title
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="")
    description = models.TextField()
    responsible = models.ForeignKey(User, on_delete=models.DO_NOTHING)