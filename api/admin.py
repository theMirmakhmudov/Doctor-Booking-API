from django.contrib import admin
from .models import User, News, Doctor, Date


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'role', 'is_staff')
    search_fields = ('email', 'username')
    list_filter = ('role', 'is_staff')
    list_per_page = 8
    date_hierarchy = 'created_at'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_per_page = 8
    search_fields = ('title',)
    date_hierarchy = 'created_at'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'specialization', 'experience', 'location', 'clinic_name', 'consultation_fee', 'is_consultation_free',
        'availability_today', 'rating_percentage', 'patient_stories')
    list_per_page = 8
    search_fields = ('specialization', 'clinic_name')
    date_hierarchy = 'created_at'


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'status', 'time', 'date')
    list_per_page = 8
    date_hierarchy = 'created_at'
