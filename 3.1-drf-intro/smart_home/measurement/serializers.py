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


class MeasurementSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['sensor_id', 'temperature', 'created_at']


class InfoSensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensors
        fields = ['id', 'name', 'description', 'measurements']
