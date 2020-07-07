from django.urls import path

from myapp import views

urlpatterns = [
path('', views.SetReminder.as_view(), name='setreminder'),
path('view_reminder', views.view_reminder, name='viewreminder'),
path('edit_reminder/<int:pk>', views.EditReminder.as_view(), name='editdata'),
path('delete_reminder/<int:pk>', views.DeleteReminder.as_view(), name='deletedata'),
]
