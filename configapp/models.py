from django.db import models
from django.core.exceptions import ValidationError

class BaseModel(models.Model):
    created_ed=models.DateTimeField(auto_now_add=True)
    updated_ed=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True


class Subject(BaseModel):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name=models.CharField(max_length=150)
    phone=models.CharField(max_length=15)
    location=models.CharField(max_length=255)
    subject=models.ForeignKey(Subject , on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
