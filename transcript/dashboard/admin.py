from . models import *
from import_export.admin import ImportExportModelAdmin
from django.urls import path
from django.shortcuts import redirect
from django.contrib import admin
from django.shortcuts import reverse, render
from django.utils.html import format_html
from django.shortcuts import redirect
from django.urls import path
from .models import Year, Class


class StudentAdmin(ImportExportModelAdmin):
    list_display = ["studentid", "firstname","lastname","dateofbirth" ]
    search_fields = ["studentid"]
    list_per_page = 9
    pass

class ScoreInline(admin.TabularInline):
    model = Score

#edit


class YearAdmin(admin.ModelAdmin):
        list_display = ["year"]
        list_display_links = None  # Remove the link from the year field


class ClassAdmin(admin.ModelAdmin):
    list_filter = ["year"]
    #inlines = [ScoreInline]


class ScoreAdmin(admin.ModelAdmin):
    list_display = ["student", "yearid", "classes_taken", "score", "calculate_gpa"]
    search_fields = ["student"]
    list_per_page = 9

class academicyearAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(academicyear, academicyearAdmin)





