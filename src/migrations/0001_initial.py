# Generated by Django 2.2.7 on 2020-03-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.CharField(max_length=20)),
                ('User_Name', models.CharField(max_length=20)),
                ('User_Password', models.CharField(max_length=20)),
            ],
        ),
    ]
