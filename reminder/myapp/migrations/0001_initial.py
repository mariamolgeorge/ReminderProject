# Generated by Django 2.2.5 on 2020-07-07 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReminderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_date', models.DateField()),
                ('reminder_time', models.TimeField()),
                ('remider_data', models.CharField(max_length=200)),
            ],
        ),
    ]
