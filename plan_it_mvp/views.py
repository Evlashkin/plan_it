from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import JobSerializer
from .models import Job


# Create your views here.

# Данный класс описывает, что будет возвращать метод GET. В нашем случае массивв всех работ
class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    # authentication_classes = (TokenAuthentication,)  # Эта строка отвечает за выдачу результата, если знаешь токен

    # Строка кода ниже позволяет использовать REST API только прошедшим аутентификацию пользователям,
    # несмотря на то, что в settings установлено 'rest_framework.permissions.AllowAny'. Таким образом, мы можем
    # разделять разные методы REST по правам. (Например: просмотр работ открыт для всех, а вот просмотр users, только
    # для тех, кто прошел аутентификацию)
    permission_classes = (IsAuthenticated,)
