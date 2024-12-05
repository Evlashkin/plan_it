from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
# class Account(models.Model): pass - не нужен, т.к. Django дает юзера по умолчанию


class ProjectParticipants(models.Model):
    pp_name = models.CharField(max_length=150)
    pp_ac = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    # pp_roles = Указал его в классе Role
    is_virtual = models.BooleanField(default=False)

    def __str__(self):
        return self.pp_name


class Project(models.Model):
    # jobs = Указал его в классе Job
    # hard_links = Указал его в классе HardLink
    # proj_participants = models. Тут непонятно
    # proj_templates = Указал его в классе ProjectTemplate
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)


class HardLink(models.Model):
    job_source = models.CharField(max_length=150)
    job_target = models.CharField(max_length=150)
    projects = models.ForeignKey(Project, related_name='hard_links', on_delete=models.CASCADE)


class ProjectTemplate(models.Model):
    project = models.ForeignKey(Project, related_name='proj_templates', on_delete=models.CASCADE)

    # jobs = Указал его в классе HardLinkTemplate
    # pt_roles = Указал его в классе Role
    # hard_links = Указал его в классе HardLinkTemplate


class JobTemplate(models.Model):
    jt_class = models.CharField(max_length=150)
    jt_name = models.CharField(max_length=150)
    out_ready = models.CharField(max_length=150)
    in_ready = models.CharField(max_length=150)
    jt_start = models.DateTimeField(default=timezone.now)
    jt_duration = models.CharField(max_length=150, blank=True)
    jt_end = models.DateTimeField(default=timezone.now, null=True, blank=True)
    pt_id = models.OneToOneField(ProjectTemplate, on_delete=models.CASCADE)
    jt_processing_role = models.CharField(max_length=150, blank=True)
    jt_prev = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='prev_jobs')
    jt_next = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='next_jobs')
    project_templates = models.ForeignKey(ProjectTemplate, null=True, blank=True, related_name='jobs', on_delete=models.SET_NULL)

    def __str__(self):
        return self.jt_name


class HardLinkTemplate(models.Model):
    jobt_source = models.CharField(max_length=150)
    jobt_target = models.CharField(max_length=150)
    project_templates = models.ForeignKey(ProjectTemplate, null=True, blank=True, related_name='hard_links', on_delete=models.SET_NULL)

    def __str__(self):
        return self.jobt_source + '_' + self.jobt_target


class Role(models.Model):
    role_name = models.CharField(max_length=150)
    # job_class = Указал его в классе JobClass
    project_template = models.ForeignKey(ProjectTemplate, null=True, blank=True, related_name='pt_roles', on_delete=models.SET_NULL)
    project_participants = models.ForeignKey(ProjectParticipants, null=True, blank=True, related_name='pp_roles', on_delete=models.SET_NULL)

    def __str__(self):
        return self.role_name


class JobClass(models.Model):
    jc_name = models.CharField(max_length=150)
    roles = models.ForeignKey(Role, related_name='job_class', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.jc_name


class Job(models.Model):
    # related_name указывает на то, как будет называться атрибут в Job
    job_class = models.ForeignKey(JobClass, on_delete=models.CASCADE, related_name='jobs')
    job_name = models.CharField(max_length=150)
    out_ready = models.CharField(max_length=150, blank=True)
    in_ready = models.CharField(max_length=150, blank=True)
    job_start = models.DateTimeField(default=timezone.now)
    job_duration = models.CharField(max_length=150, blank=True)
    job_end = models.DateTimeField(default=timezone.now, null=True, blank=True)
    proj_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='jobs')
    # В строке ниже отношение: многие ко многим. Но показывать их нужно только с фильтром по проекту. Пока не знаю как.
    job_processing_unit = models.ManyToManyField(ProjectParticipants, related_name='jobs')
    job_prev = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='prev_jobs')
    job_next = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='next_jobs')

    def __str__(self):
        return self.job_name
