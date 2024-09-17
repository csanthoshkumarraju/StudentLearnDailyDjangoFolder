# Generated by Django 5.1.1 on 2024-09-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studenthomeworkapp', '0002_studenthomeworkmodel_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenthomeworkmodel',
            name='status',
            field=models.CharField(default='To do', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='studenthomeworkmodel',
            name='subject_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='studenthomeworkmodel',
            name='topic_name',
            field=models.TextField(null=True),
        ),
    ]
