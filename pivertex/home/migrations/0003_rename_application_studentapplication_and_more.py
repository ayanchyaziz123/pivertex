# Generated by Django 5.0.3 on 2024-03-11 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_consultant_university_course_application'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Application',
            new_name='StudentApplication',
        ),
        migrations.AlterField(
            model_name='client',
            name='client_type',
            field=models.CharField(choices=[('student', 'Student'), ('institution', 'Institution'), ('reguler', 'reguler'), ('other', 'Other')], default='student', max_length=20),
        ),
        migrations.CreateModel(
            name='RegularApplication',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('application_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.client')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.consultant')),
            ],
        ),
    ]
