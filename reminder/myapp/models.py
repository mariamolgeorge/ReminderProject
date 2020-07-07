from django.db import models
class ReminderData(models.Model):
    """This is for adding reminder  """
    reminder_date=models.DateField()
    reminder_time=models.TimeField()
    remider_data=models.CharField(max_length=200)


    def __str__(self):
        return self.reminder_date
# Create your models here.
