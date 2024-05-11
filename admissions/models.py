from django.db import models

class Department(models.Model):
  departmentId = models.AutoField(primary_key=True)
  departmentName = models.CharField(max_length=100)

  class Meta:
    abstract = True