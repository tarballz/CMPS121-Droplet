# Tutorial said to add these.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from teams.models import Team
from teams.serializers import TeamSerializer
# End

from rest_framework import viewsets



class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# More shit the tutorial is telling me to add
# "The root of our API is going to be a view that supports
#  listing all the existing teams, or creating a new team"

@api_view(['GET', 'POST'])
def team_list(request, format=None):
    """
    List all teams, or create new team
    """
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk, format=None):
    """
    Retrieve, update or delete a team
    """
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
