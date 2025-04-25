from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-end_date')
    serializer_class = ProjectSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['request'] = self.request
        return ctx
