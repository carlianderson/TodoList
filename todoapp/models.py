from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.category_name)

    class Meta:
        db_table='category'

class TodoList(models.Model):
    task=models.CharField(max_length=255)
    created_date=models.DateField()
    due_date=models.DateField()
    category_id = models.ForeignKey(Category, default="personal", on_delete=models.CASCADE) 

    def __str__(self):
        return self.task

    class Meta:
        db_table='todolist'