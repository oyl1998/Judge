# Generated by Django 2.2.7 on 2020-03-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20200326_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='Problem_Description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='problem',
            name='Problem_Hint',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='problem',
            name='Problem_Input',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='problem',
            name='Problem_Output',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='problem',
            name='Problem_Sample_Program',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='problem',
            name='Problem_Simple_Input',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='problem',
            name='Problem_Simple_Output',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='problem',
            name='Problem_Source',
            field=models.CharField(default='', max_length=100),
        ),
    ]
