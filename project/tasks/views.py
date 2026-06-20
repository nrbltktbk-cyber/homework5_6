from rest_framework import viewsets
from .models import Task
from .serializers import TaskListSerializer, TaskDetailSerializer

class TaskViewSet(viewsets.ModelViewSet):
   
    queryset = Task.objects.select_related('category').prefetch_related('tags').all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        return TaskDetailSerializer
