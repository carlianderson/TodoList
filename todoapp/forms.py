from django import forms
from .models import Category, TodoList

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model=TodoList
        fields='__all__'