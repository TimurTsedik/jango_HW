from django.urls import path

from .views import SensorsView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:sensor_id>/', MeasurementView.as_view()),
    path('sensors/<int:sensor_id>/<str:sensor_description>/', SensorsView.as_view()),
    path('sensors/<str:sensor_name>/<str:sensor_description>/', SensorsView.as_view()),
    path('measurements/<int:sensor_id>/<str:temp_value>/', MeasurementView.as_view()),
]
