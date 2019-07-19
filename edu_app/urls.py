from django.urls import path
from edu_app import views

urlpatterns = [
    path('', views.indexAdmin),

]
