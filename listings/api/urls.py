from django.urls import include, path

from . import views


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("houses/", views.HouseList.as_view()),
    path("houses/<int:pk>", views.HouseDetail.as_view()),
]
