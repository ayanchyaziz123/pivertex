from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Document)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(Consultant)
admin.site.register(StudentApplication)
admin.site.register(StudentApplicationStatus)
