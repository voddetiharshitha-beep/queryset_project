from django.urls import path

from .n_plus_one import inefficient_rides
from .history import ride_history
from .active import active_rides
from .completed import completed_rides
from .cancelled import cancelled_rides
from .n_plus_one_optimized import optimized_rides
from . import views


urlpatterns = [

    path(
        "",
        views.ride_list,
        name="ride-list"
    ),

    path(
        "history/",
        ride_history,
        name="ride-history"
    ),

    path(
        "active/",
        active_rides,
        name="active-rides"
    ),

    path(
        "completed/",
        completed_rides,
        name="completed-rides"
    ),

    path(
        "cancelled/",
        cancelled_rides,
        name="cancelled-rides"
    ),

    path(
        "n-plus-one/",
        inefficient_rides,
        name="n-plus-one"
    ),

    path(
        "n-plus-one-optimized/",
        optimized_rides,
        name="n-plus-one-optimized"
    ),

    path(
        "aggregation/",
        views.ride_aggregation,
        name="ride-aggregation"
    ),
]