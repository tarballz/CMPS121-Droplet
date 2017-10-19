from teams.models import Team
from teams.serializers import TeamSerializer
from rest_framework import generics, viewsets


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_fields = ('name')
