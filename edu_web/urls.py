from django.urls import path
from edu_web import views

urlpatterns = [
    path('', views.indexAdmin),
    path('web/error.html',views.error)
]
