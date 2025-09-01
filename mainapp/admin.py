from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.BaseDetail)
admin.site.register(models.Homepage)
admin.site.register(models.Team)
admin.site.register(models.AboutUs)
admin.site.register(models.JobOpening)
admin.site.register(models.ContactUs)
admin.site.register(models.Project)