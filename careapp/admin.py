from django.contrib import admin

from careapp.models import *

# Register your models here.
admin.site.register(MyAppoinments)
admin.site.register(Doctor)
admin.site.register(Patients)
admin.site.register(Transaction)
