from django.urls import path
from . import views

urlpatterns = [
        path("", views.all_universities),
        path("<int:id>", views.get_universities_data),
        path("create/", views.create_university),
        path("del_university/<int:id>", views.del_university),
        ]
