# Generated by Django 2.1.3 on 2018-11-18 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beno', '0005_auto_20181118_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-due_by', 'priority']},
        ),
    ]
