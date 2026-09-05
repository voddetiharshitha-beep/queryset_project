
"""
URL configuration for queryset_project project.
"""

from django.contrib import admin
from django.urls import path, include
from students import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/students/aggregation/",
        views.student_aggregation,
        name="student-aggregation",
    ),

    path(
        "api/rides/",
        include("students.urls"),
    ),
]
