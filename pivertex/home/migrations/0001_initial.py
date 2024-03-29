# Generated by Django 5.0.3 on 2024-03-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='client_documents/')),
                ('description', models.TextField(blank=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
                ('current_location', models.CharField(max_length=100)),
                ('client_type', models.CharField(choices=[('student', 'Student'), ('institution', 'Institution'), ('parent', 'Parent'), ('other', 'Other')], default='student', max_length=20)),
                ('documents', models.ManyToManyField(blank=True, related_name='clients', to='home.document')),
            ],
        ),
    ]
