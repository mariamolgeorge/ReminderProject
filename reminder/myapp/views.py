from django.shortcuts import render
from myapp.models import ReminderData
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView,DeleteView
class SetReminder(CreateView):
    model=ReminderData

    fields=['reminder_date','reminder_time','remider_data']

    template_name = 'setreminder.html'
    success_url=reverse_lazy('setreminder')
def view_reminder(request):

    obj=ReminderData.objects.all()
    data={}
    data['object']=obj


    return render(request,'view_reminder.html',data)
# Create your views here.



class EditReminder(UpdateView):
    model = ReminderData
    fields=['reminder_date','reminder_time','remider_data']
    template_name = 'edit_reminder.html'
    success_url = reverse_lazy('viewreminder')
class DeleteReminder(DeleteView):
    model = ReminderData
    fields='__all__'
    template_name = 'delete_reminder.html'
    success_url = reverse_lazy('viewreminder')