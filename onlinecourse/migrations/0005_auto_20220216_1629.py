# Generated by Django 3.1.3 on 2022-02-16 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20211013_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.instructor')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(through='onlinecourse.Course_Instructor', to='onlinecourse.Instructor'),
        ),
    ]
