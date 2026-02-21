from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    


class Employee(models.Model):
    fullname = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    


class user_reg(models.Model):
    username = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.SmallIntegerField(default=1)
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_reg"


