from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('todo/', views.todo, name='todo'),
   path('tododetail/<int:id>', views.tododetail, name='detail'),
   path('newtask/', views.newTask, name='newtask'),
   path('newcategory/', views.newCategory, name='newcategory'),
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   path('logoutmessage/', views.logoutmessage, name='logoutmessage'), 
]