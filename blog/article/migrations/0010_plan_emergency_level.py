# Generated by Django 2.0.4 on 2018-05-22 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20180521_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='emergency_level',
            field=models.IntegerField(choices=[(0, '有空在做'), (1, '正常处理'), (2, '优先处理'), (3, '十万火急')], default=1),
        ),
    ]
