# Generated by Django 4.1.5 on 2024-02-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDMSapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stud_item',
            name='item_id',
        ),
        migrations.AddField(
            model_name='stud_item',
            name='item_id',
            field=models.ManyToManyField(to='SDMSapp.item'),
        ),
    ]
