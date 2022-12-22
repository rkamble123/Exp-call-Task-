from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("LCUser_api/",views.LCUser_api.as_view(),name = 'LCUser_api'),
    path("RUDUser_api/<int:pk>",views.RUDUser_api.as_view(),name = 'RUDUser_api'),
    path("auth/",include('rest_framework.urls',namespace='rest_framework')),
    path("gettoken/",obtain_auth_token),


]