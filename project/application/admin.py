from django.contrib import admin
from .models import Province, City, Barangay, Survey

admin.site.register(Province)
admin.site.register(City)
admin.site.register(Barangay)
admin.site.register(Survey)