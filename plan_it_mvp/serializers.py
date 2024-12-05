from rest_framework import serializers
from .models import Job

# REST API - указываем в классе из какой модели, какие поля показывать. В нашем случае при вызове метода GET
# будут возвращены только атрибуты "job_name" и "job_class"
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["job_name", "job_class"]
