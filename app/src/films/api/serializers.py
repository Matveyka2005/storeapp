from rest_framework import serializers

from ..models import Film


class FilmSerializer(serializers.ModelSerializer):
    rate = serializers.DecimalField(max_digits=3, decimal_places=2)
    class Meta:
        model = Film
        fields = ('name', 'about', 'image', 'video', 'author', 'category', 'rate')