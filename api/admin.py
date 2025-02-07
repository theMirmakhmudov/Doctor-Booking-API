from django.contrib import admin
from .models import User, News, Doctor, Date

admin.site.register(User)
admin.site.register(News)
admin.site.register(Doctor)
@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'status', 'time', 'date')