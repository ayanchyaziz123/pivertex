from django.db import models

class ClientType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    current_location = models.CharField(max_length=100)
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE)
    documents = models.ManyToManyField('Document', related_name='clients', blank=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='client_documents/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
class University(models.Model):
    university_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class Consultant(models.Model):
    consultant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    expertise_area = models.CharField(max_length=100)

class StudentApplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    application_date = models.DateField()
 

class StudentApplicationStatus(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    describe = models.TextField()  # Add a field to describe the status (optional)
    application = models.ForeignKey(StudentApplication, on_delete=models.CASCADE)  # ForeignKey to StudentApplication model
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.get_status_display()} - {self.application}"





