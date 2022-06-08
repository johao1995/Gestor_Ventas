from django.urls import path
from . import views
usuario_urlpatterns=([
    path('home/',views.HomePage.as_view(),name='home')
],'usuario')
