from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, TodoList
import datetime
from .forms import CategoryForm, TaskForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class CategoryTest(TestCase):
    def setUp(self):
        self.category_name=Category(category_name='TestCategory')

    def test_typestring(self):
        self.assertEqual(str(self.category_name), 'TestCategory')

    def test_tablename(self):
        self.assertEqual(str(Category._meta.db_table), 'category')

class TaskTest(TestCase):
    def setUp(self):
        self.task=TodoList(task='DothisThing')

    def test_typestring(self):
        self.assertEqual(str(self.task), 'DothisThing')

    def test_tablename(self):
        self.assertEqual(str(TodoList._meta.db_table), 'todolist')

class New_Category_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newcategory'))
        self.assertRedirects(response, '/accounts/login/?next=/todoapp/newcategory/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newcategory'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todoapp/newcategory.html')