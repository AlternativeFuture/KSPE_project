from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("university.urls")),
    path("account/", include("user.urls")),
]