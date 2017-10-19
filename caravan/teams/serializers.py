from rest_framework import serializers
from teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'name',
            'cars',
        )

    def create(self, validated_data):
        """
        Create and return a new Team instance, given the
        "validated data", whatever that is.
        """
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Team instance, given
        the "validated data"
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance