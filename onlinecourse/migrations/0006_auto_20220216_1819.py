# Generated by Django 3.1.3 on 2022-02-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0005_auto_20220216_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='onlinecourse.Instructor'),
        ),
        migrations.DeleteModel(
            name='Course_Instructor',
        ),
    ]
