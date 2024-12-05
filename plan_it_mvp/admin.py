from django.contrib import admin
from .models import Job, ProjectParticipants, Project, HardLink, ProjectTemplate, JobTemplate, HardLinkTemplate, Role, JobClass


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    # в атрибуте fields явно указываем какие поля будем видеть в админке при создании/изменении
    fields = ["job_class", "job_name", "out_ready", "in_ready", "job_start", "job_duration", "job_end", "proj_id",
              "job_processing_unit", "job_prev", "job_next"]

    # указываем какие поля хотим видеть в таблице со всеми объектами
    list_display = ["job_name", "job_class", "job_start", "job_end"]

    # указываем по каким атрибутам допустима фильтация
    list_filter = ["job_class"]

    # добавляем поиск по необходимым атрибутам
    search_fields = ["job_name"]

admin.site.register(ProjectParticipants)
admin.site.register(Project)
admin.site.register(HardLink)
admin.site.register(ProjectTemplate)
admin.site.register(JobTemplate)
admin.site.register(HardLinkTemplate)
admin.site.register(Role)
admin.site.register(JobClass)
