from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

from rest_framework import serializers

from .models import Sensors, Measurements


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['id', 'sensor_id', 'temperature', 'created_at']