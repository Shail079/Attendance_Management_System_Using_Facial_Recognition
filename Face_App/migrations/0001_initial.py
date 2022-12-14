# Generated by Django 3.2.14 on 2022-08-01 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=30)),
                ('apass', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'admin_details',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default=None, null=True, upload_to='C:/PythonProjects/Facial_Recognition_Attendance/Face_Images/')),
            ],
            options={
                'db_table': 'Test',
            },
        ),
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('Class', models.CharField(max_length=100)),
                ('images', models.ImageField(default=None, upload_to='Face_Images')),
            ],
            options={
                'db_table': 'userDetails',
            },
        ),
    ]
